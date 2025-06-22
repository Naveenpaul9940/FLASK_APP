# Use a base image with Python 3.9+
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy application code
COPY . .

# Install dependencies
RUN python -m venv venv && . venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

# Expose port 5000 for Flask app
EXPOSE 5000

# Set the command to run the Flask app
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
