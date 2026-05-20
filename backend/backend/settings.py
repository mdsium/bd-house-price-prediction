"""
Django settings for backend project.
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-k7nex5@p&*gu7q^()jtx$05p6wh-#xl)6v9x+5yuh!f!jt!wn*'

DEBUG = True

ALLOWED_HOSTS = ['*']   # Change later in production

# ================== APPLICATIONS ==================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third Party
    'rest_framework',
    'drf_yasg',
    'corsheaders',           # ← Added for React frontend

    # Local Apps
    'api',
]

# ================== MIDDLEWARE ==================
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',          # ← Must be at the top
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],   # You can add templates folder later if needed
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ================== REST FRAMEWORK ==================
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}

# ================== CORS (for React) ==================
CORS_ALLOW_ALL_ORIGINS = True   # For development only

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# ================== drf-yasg Settings ==================
SWAGGER_SETTINGS = {
    'DEFAULT_INFO': 'backend.urls.swagger_info',  # We'll define this in urls.py
    'USE_SESSION_AUTH': False,
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'