#!/usr/bin/env bash
rm -rf ./htmlcov
coverage run manage.py test apps -v 2
coverage html
xdg-open ./htmlcov/index.html