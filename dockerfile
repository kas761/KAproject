# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Poetry
RUN pip install poetry

# Install dependencies
RUN poetry install --no-root

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME KARC

# Run the CLI when the container launches
CMD ["poetry", "run", "python", "app.py"]