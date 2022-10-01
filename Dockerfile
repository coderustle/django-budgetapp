# syntax=docker/dockerfile:1

ARG ENVIRONMENT=prod

# ********************************************************
# * Docker Django - BASE IMAGE                           *
# ********************************************************
FROM python:3.9-slim-bullseye AS base

ARG ENVIRONMENT

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
    pip install --no-cache-dir -r /var/tmp/requirements/${ENVIRONMENT}.txt

# ********************************************************
# * Docker Django - Multi-stage, final image             *
# ********************************************************
FROM python:3.9-slim-bullseye

# Enable SSH in Azure App Service Custom Container
ENV SSH_PASSWD "root:Docker!"

RUN --mount=type=cache,target=/var/cache/apt-final \
    apt-get update \
    && apt-get install -y --no-install-recommends dialog \
    && apt-get update \
    && apt-get install -y --no-install-recommends openssh-server \
    && echo "$SSH_PASSWD" | chpasswd

# Copy the sshd config file
COPY ./scripts/sshd_config /etc/ssh/

# Set the working directory
WORKDIR /opt/budgetapp

COPY --from=base /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy the project files
COPY . .

# Expose django port
EXPOSE 8000 2222

# Entrypoint
ENTRYPOINT [ "scripts/init.sh" ]
