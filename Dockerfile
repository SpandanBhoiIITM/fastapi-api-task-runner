# Use an official Python runtime as a base image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy all project files into the container
COPY . .

# Install FastAPI and Uvicorn directly (since no requirements.txt)
RUN pip install --no-cache-dir fastapi uvicorn

# Expose the port FastAPI runs on
EXPOSE 8000

# Command to run the FastAPI app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
