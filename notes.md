### pipenv additions
pipenv install djangorestframework - install django rest framework
pipenv install python-dotenv - install dotenv
pipenv shell !!! TO ENTER DJANGO SHELL (HIGHLY FORGOTTEN STEP) !!!

>> vscode python intepreter changed to local project Django intepreter

### Django apps created
python manage.py startapp accounts
python manage.py startapp applications
python manage.py startapp api
mkdir templates

### from jobtracker>settings.py
imports:
    import os
    from dotenv import load_dotenv
    load_dotenv()
    ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")

in installed apps: 
    "rest_framework",
    "accounts",
    "applications",
    "api",

in templates:
    "DIRS": [BASE_DIR / "templates"],
        "OPTIONS": {
        "context_processors": [
            "django.template.context_processors.debug",

ROOT_URLCONF = "jobtracker.urls"
WSGI_APPLICATION = "jobtracker.wsgi.application"

LOGIN_REDIRECT_URL = "applications:list"  
LOGOUT_REDIRECT_URL = "login"
LOGIN_URL = "login"
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"