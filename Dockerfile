# Use the official Python image from the Docker Hub
FROM python:3.11.2-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Install any dependencies specified in requirements.txt
COPY todoapp/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY todoapp .

# Set environment variable to avoid buffering
ENV PYTHONUNBUFFERED=1

# Expose the port the app runs on
EXPOSE 8000
EXPOSE 8001

# Run the command to start the Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
