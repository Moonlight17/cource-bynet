#!/bin/bash

# Collect static files
# echo "Collect static files"
# python manage.py collectstatic --noinput

# Apply database system's tables
echo "Apply system's tables"
python manage.py makemigrations
python manage.py migrate

# Apply database application's tables
echo "Apply application's tables"
python manage.py makemigrations aggregated
python manage.py migrate aggregated

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:${BACKEND_PORT}
