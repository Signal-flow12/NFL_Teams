#!/usr/bin/env bash

pip3 install -r deps.txt

python manage.py migrate

python3 manage.py collectstatic --no-input