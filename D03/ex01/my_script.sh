#!/bin/sh
pip3 install virtualenv
virtualenv my_virtualenv
pip3 install git+https://github.com/jaraco/path.git -t ./local_lib --log installation.log
python3 my_program.py