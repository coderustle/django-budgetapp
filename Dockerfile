# syntax=docker/dockerfile:1

ARG ENVIRONMENT=prod
# ********************************************************
# * Docker Django - Multi-stage, base image             *
# ********************************************************
FROM python:3.9-slim-bullseye AS base

ARG ENVIRONMENT

# Set the working directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Update the system
RUN apt-get update && \
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

# Create a new user
RUN useradd --create-home budget

# From now on, run all the commands with this user
USER budget

# Set the working directory
WORKDIR /home/budget

COPY --from=base /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy the project files
COPY . .

# Expose django port
EXPOSE 8000

# Run Django application
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
ENTRYPOINT [ "scripts/init.sh" ]
