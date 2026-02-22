import os
from django.core.wsgi import get_wsgi_application

# 1. Set the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eac_project.settings')

# 2. Define 'application' FIRST
application = get_wsgi_application()

# 3. Define 'app' SECOND (Vercel looks for this specifically)
app = application
