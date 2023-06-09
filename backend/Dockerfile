# Use an official Python runtime as the base image
FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y libpq-dev build-essential

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire backend directory to the working directory
COPY . .

# Expose the desired port (adjust if necessary)
EXPOSE 8000

# Set the command to run the backend server
CMD ["python", "app/run.py"]
