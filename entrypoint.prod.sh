#!/bin/sh

python manage.py makemigrations
python manage.py migrate --no-input
python manage.py collectstatic --no-input

DEFAULT_PORT=8000
PORT=${PORT:-$DEFAULT_PORT}

gunicorn config.wsgi:application --bind 0.0.0.0:$PORT