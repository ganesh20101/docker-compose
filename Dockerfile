FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required Python packages including Flask, MySQL connector, and gunicorn
RUN pip install flask mysql-connector-python gunicorn

# Use gunicorn to serve the Flask app on port 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]

