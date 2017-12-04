#!/usr/bin/env bash
export DEBUG=True
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
