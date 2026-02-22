#!/bin/bash

echo "Building project..."

# Force install requirements to bypass the 'managed environment' error
python3.12 -m pip install -r requirements.txt --break-system-packages

# Create the folder Vercel is looking for
mkdir -p staticfiles_build/static

# Run migrations and collect static files
python3.12 manage.py collectstatic --noinput --clear

echo "Build complete."