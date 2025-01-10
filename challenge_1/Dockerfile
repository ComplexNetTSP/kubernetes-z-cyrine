# Use the official Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application files into the container
COPY app.py /app/

# Install Flask
RUN pip install flask

# Expose the application port
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
