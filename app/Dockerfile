# Use an official Python runtime as base image
FROM python:3.11-slim

# Prevent .pyc files; and set unbuffered to get logs in real-time
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project files
COPY . /app/

# Expose port 8000 (the Django default)
EXPOSE 8000

# Set the default command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
