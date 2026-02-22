# EAC Lost & Found System

A modern, responsive web application for managing lost and found items at Emilio Aguinaldo College - Cavite.

## Features

- 📱 **Responsive Design** - Works seamlessly on mobile, tablet, and desktop
- 🔐 **Role-Based Access** - Different permissions for students and administrators
- 🔍 **Advanced Search** - Filter by category, date, and keywords
- 🎨 **Modern UI** - Glassmorphism effects and clean design
- 👤 **User Authentication** - Secure login and registration system

## Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (development)
- **Authentication**: Django Auth

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/EAC_LostAndFound.git
cd EAC_LostAndFound
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install django pillow
```

4. Run migrations:

```bash
python manage.py migrate
```

5. Create a superuser:

```bash
python manage.py createsuperuser
```

6. Run the development server:

```bash
python manage.py runserver
```

7. Visit `http://localhost:8000` in your browser

## Usage

### For Students

- Report lost items with details and photos
- Search for found items
- View recovery history

### For Administrators

- All student features
- Mark items as found
- Manage all reported items

## Project Structure

```
EAC_LostAndFound/
├── lost_found/          # Main app
│   ├── models.py        # Database models
│   ├── views.py         # View logic
│   ├── urls.py          # URL routing
│   ├── templates/       # HTML templates
│   └── static/          # CSS, JS, images
├── EAC_LostAndFound/    # Project settings
└── manage.py            # Django management script
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is created for educational purposes at Emilio Aguinaldo College - Cavite.
