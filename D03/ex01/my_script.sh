#!/bin/bash
pip3 -V
pip3 install git+https://github.com/jaraco/path.git -t ./local_lib --log installation.log --upgrade
python3 my_program.py