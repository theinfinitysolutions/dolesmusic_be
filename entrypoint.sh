#!/bin/bash

# Run database migrations
python manage.py makemigrations
python manage.py migrate

# Create the OAuth2 app
python manage.py create_oauth2_app

# Start the background process for abandoned cart notifications
nohup sh -x send_abandoned_cart_notification.sh > log_file.txt 2>&1 &

# Start the Django development server (or replace with Gunicorn for production)
python manage.py runserver 0.0.0.0:80