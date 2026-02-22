#!/bin/bash

echo "Building the project..."

# 1. Install dependencies using the override flag
python3.12 -m pip install -r requirements.txt --break-system-packages

# 2. Create the output directory manually
mkdir -p staticfiles_build/static

# 3. Run migrations and collect static files
python3.12 manage.py migrate --noinput
python3.12 manage.py collectstatic --noinput --clear

echo "Build finished successfully."