#!/bin/bash

# Run necessary Django commands
echo "Running Django migrations..."
python manage.py makemigrations
python manage.py migrate --no-input
python manage.py collectstatic --no-input

# Set up port configuration
DEFAULT_PORT=8000
PORT=${PORT:-$DEFAULT_PORT}

# Start Gunicorn
echo "Starting Gunicorn..."
gunicorn config.wsgi:application --bind 0.0.0.0:$PORT

# Check if Gunicorn started successfully
if [ $? -ne 0 ]; then
    echo "Failed to start Gunicorn."
    exit 1
fi

echo "Django application is running on port $PORT."
