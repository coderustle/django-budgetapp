# syntax=docker/dockerfile:1

# requirements.txt file to install in virtual environment
ARG PYTHON_REQUIREMENTS_FILE=prod

# ********************************************************
# * Docker Django - BASE IMAGE                           *
# ********************************************************
FROM python:3.11-slim-bullseye AS base

ARG PYTHON_REQUIREMENTS_FILE

# Set the working directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Update the system
RUN --mount=type=cache,target=/var/cache/apt-base \
    apt-get update && \
    apt-get install -y --no-install-recommends gcc

# Create virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy the project files
COPY requirements /var/tmp/requirements

# Install python packages
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r /var/tmp/requirements/${PYTHON_REQUIREMENTS_FILE}.txt

# Download the static build of Litestream directly into the path & make it executable.
# This is done in the builder and copied as the chmod doubles the size.
ADD https://github.com/benbjohnson/litestream/releases/download/v0.3.11/litestream-v0.3.11-linux-amd64.tar.gz /tmp/litestream.tar.gz
RUN tar -C /usr/local/bin -xzf /tmp/litestream.tar.gz

# ********************************************************
# * Docker Django - TEST                                 *
# ********************************************************
FROM python:3.11-slim-bullseye AS development

# Build parameters
ARG DJANGO_SETTINGS_MODULE
ARG SECRET_KEY

ENV DJANGO_SETTINGS_MODULE=${DJANGO_SETTINGS_MODULE}
ENV SECRET_KEY=${SECRET_KEY}

# Set the working directory
WORKDIR /opt/project_name

# Copy build from base
COPY --from=base /opt/venv /opt/venv
COPY --from=base /usr/local/bin/litestream /usr/local/bin/litestream

ENV PATH="/opt/venv/bin:$PATH"

# Copy the project files
COPY . .
COPY ./litestream.yml /etc/litestream.yml

# Expose Django port
EXPOSE 8000

# ********************************************************
# * Docker Django - PRODUCTION                           *
# ********************************************************
FROM python:3.11-slim-bullseye

# Enable SSH in Azure App Service Custom Container
# The passowrd is standard for Azure and needs to be like this
ENV SSH_PASSWD "root:Docker!"

RUN --mount=type=cache,target=/var/cache/apt-production \
    apt-get update \
    && apt-get install -y --no-install-recommends dialog \
    && apt-get update \
    && apt-get install -y --no-install-recommends openssh-server \
    && echo "$SSH_PASSWD" | chpasswd

# Copy the sshd config file
COPY ./scripts/sshd_config /etc/ssh/

# Set the working directory
WORKDIR /opt/budgetapp

# Copy build from base
COPY --from=base /opt/venv /opt/venv
COPY --from=base /usr/local/bin/litestream /usr/local/bin/litestream

ENV PATH="/opt/venv/bin:$PATH"

# Copy the project files
COPY . .
COPY ./litestream.yml /etc/litestream.yml

# Expose django port
EXPOSE 8000 2222

# Entrypoint
ENTRYPOINT [ "scripts/init.sh" ]
