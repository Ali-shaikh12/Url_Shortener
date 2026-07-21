# Url_Shortener
A Django-based URL shortener web app that lets users create custom short links, redirect visitors to original URLs, and track link analytics including total clicks, device type, country data, and last click activity.

# Features
- Create custom short URL aliases
- Redirect short links to their original URLs
- Track total clicks for each short link
- Record country-based click counts from request headers
- Detect desktop and mobile clicks from the user agent+
- View analytics charts for countries and device types
- Copy generated short links from the browser

# Tech Stack

- Python
- Django
- SQLite
- HTML
- CSS
- Bootstrap
- Chart.js

## Project Structure

```text
Url_Shortener/
├── manage.py
├── requirements.txt
├── Url_Shortener/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── myapp/
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── templates/
    ├── static/
    └── migrations/
```

## Setup

1. Clone the repository.

```bash
git clone <repository-url>
cd Url_Shortener
```

2. Create and activate a virtual environment.

```bash
python -m venv myvenv
myvenv\Scripts\activate
```

3. Install dependencies.

```bash
pip install -r requirements.txt
```

4. Run migrations.

```bash
python manage.py migrate
```

5. Start the development server.

```bash
python manage.py runserver
```

6. Open the app in your browser.

```text
http://127.0.0.1:8000/
```

## Environment Variables

For production or shared deployments, set a secure Django secret key:

```bash
set DJANGO_SECRET_KEY=your-secret-key
```

