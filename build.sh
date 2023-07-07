#!/usr/bin/env bash
# exit on error
# Dependencies Installation
set -o errexit

pip3 install -r deps.txt

python manage.py collectstatic --no-input
python manage.py migrate