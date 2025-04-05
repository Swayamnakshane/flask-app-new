# Use the official Python image
FROM python:3.9-slim
#FROM python:3.11-alpine

# Set the working directory
WORKDIR /app

# Copy requirements first and install
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Set the environment variable for Flask
ENV FLASK_APP=app.py

# Expose the port the app runs on
EXPOSE 5000

# Run the app
CMD ["flask", "run", "--host=0.0.0.0"]

