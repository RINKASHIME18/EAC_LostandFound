import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eac_project.settings')
django.setup()

from django.contrib.auth import get_user_model

def ensure_admin():
    User = get_user_model()
    # Using the credentials you requested
    username = 'admin'
    email = 'admin@example.com'
    password = 'admin'

    if not User.objects.filter(username=username).exists():
        print(f"Creating superuser '{username}' for Railway...")
        User.objects.create_superuser(username, email, password)
        print("Superuser created successfully.")
    else:
        # We update the password just in case it was lost
        user = User.objects.get(username=username)
        user.set_password(password)
        user.save()
        print(f"Superuser '{username}' already exists. Password verified.")

if __name__ == "__main__":
    ensure_admin()
