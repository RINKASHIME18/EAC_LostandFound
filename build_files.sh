#!/bin/bash
echo "Building project..."
python3.12 -m pip install -r requirements.txt --break-system-packages
export PYTHONPATH=$PYTHONPATH:.
python3.12 manage.py collectstatic --noinput --clear
echo "Build complete."
