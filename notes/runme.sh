#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Run Django management commands
echo "Running makemigrations..."
python3 manage.py makemigrations

echo "Running migrate..."
python3 manage.py migrate

echo "Starting Django development server..."
python3 manage.py runserver 0.0.0.0:8000