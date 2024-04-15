# Base image: Official Python runtime
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Flask app file into the container at /app
COPY app.py /app

# Install Flask using pip
RUN pip install Flask


# Expose the port the app runs on
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "app.py"]
