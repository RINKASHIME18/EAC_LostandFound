import os
from django.core.wsgi import get_wsgi_application

# 1. Point to your settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eac_project.settings')

# 2. CREATE the application variable (Django does this)
application = get_wsgi_application()
