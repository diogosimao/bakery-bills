#!/usr/bin/env bash
export DEBUG=True
export DATABASE_URL=psql://postgres:postgres@127.0.0.1:5432/bakery-bills
export HIDE_DOCS=False
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
