#!/bin/zsh

gunicorn -c conf/gunicorn_config.py d08.wsgi