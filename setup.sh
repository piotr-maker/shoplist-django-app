#!/bin/bash

echo Creating virtual environment...
python3 -m venv env

echo Installing requirenments...
source env/bin/activate
pip3 install -r requirements.txt
