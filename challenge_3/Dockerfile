# Use the official Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application files into the container
COPY app.py /app/

# Installation des dépendances
RUN pip install flask pymongo

# Expose the application port
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
