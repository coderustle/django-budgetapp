FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy all the project files
COPY . .

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install python packages
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r ./requirements/local.txt

# Expose django port
EXPOSE 8000

# Run Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]