#!/bin/sh

pip3 install virtualenv
python3 -m virtualenv django_venv
#virtualenv -p ${which python3} django_venv
source django_venv/bin/activate
pip3 install -r requirement.txt