# syntax=docker/dockerfile:1

# Used to specify the requirements.txt
ARG BUILD_ENV=prod

# ********************************************************
# * Docker Django - BASE IMAGE                           *
# ********************************************************
FROM python:3.10-slim-bullseye AS base

ARG BUILD_ENV

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
    pip install --no-cache-dir -r /var/tmp/requirements/${BUILD_ENV}.txt

# ********************************************************
# * Docker Django - TEST                                 *
# ********************************************************
FROM python:3.10-slim-bullseye AS development

# Build parameters
ARG DJANGO_SETTINGS_MODULE
ARG SECRET_KEY
ARG DB_NAME
ARG DB_HOST
ARG DB_PASS
ARG DB_USER

ENV DJANGO_SETTINGS_MODULE=${DJANGO_SETTINGS_MODULE}
ENV SECRET_KEY=${SECRET_KEY}
ENV DB_NAME=${DB_NAME}
ENV DB_HOST=${DB_HOST}
ENV DB_PASS=${DB_PASS}
ENV DB_USER=${DB_USER}

# Set the working directory
WORKDIR /opt/project_name

# Copy build from base
COPY --from=base /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy the project files
COPY . .

# Expose Django port
EXPOSE 8000

# ********************************************************
# * Docker Django - PRODUCTION                           *
# ********************************************************
FROM python:3.10-slim-bullseye

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
ENV PATH="/opt/venv/bin:$PATH"

# Copy the project files
COPY . .

# Expose django port
EXPOSE 8000 2222

# Entrypoint
ENTRYPOINT [ "scripts/init.sh" ]
