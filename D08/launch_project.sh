#!/bin/zsh

python3 d08/manage.py makemigrations
python3 d08/manage.py migrate
python3 d08/manage.py collectstatic