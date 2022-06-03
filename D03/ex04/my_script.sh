#!/bin/sh

pip3 install virtualenv
virutalenv virtualenv -p ${which python3} django_venv
pip3 install -r requirement.txt
source django_venv/bin/activate