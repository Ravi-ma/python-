# Use an official Python version as the base image
FROM python:3.10-slim

# Set environment variables to prevent Python from writing .pyc files and buffer stdout
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the working directory
COPY . .

# Expose port 5000 for Flask to run on
EXPOSE 5000

# Set Flask app environment variables
ENV FLASK_APP=pythoncode.py
ENV FLASK_ENV=development

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
