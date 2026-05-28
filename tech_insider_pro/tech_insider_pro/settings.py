from pathlib import Path
import os
# import cloudinary
# import cloudinary.uploader
# import cloudinary.api

BASE_DIR = Path(__file__).resolve().parent.parent

# ========================
# SECURITY
# ========================

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "change-this-in-production")

DEBUG = os.getenv("DEBUG", "False").lower() == "true"

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    ".onrender.com",
]

# ========================
# APPS
# ========================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',

    'mainapp',

    'django_ckeditor_5',
    'cloudinary',
    'cloudinary_storage',
]

# ========================
# MIDDLEWARE
# ========================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tech_insider_pro.urls'

# ========================
# TEMPLATES
# ========================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'tech_insider_pro.wsgi.application'

# ========================
# DATABASE
# ========================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ========================
# PASSWORD VALIDATION
# ========================

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ========================
# INTERNATIONALIZATION
# ========================

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

# ========================
# STATIC FILES
# ========================

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'mainapp' / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ========================
# MEDIA (IMPORTANT FIX)
# ========================

# CLOUDINARY_STORAGE = {
#     "CLOUD_NAME": os.getenv("CLOUDINARY_CLOUD_NAME", ""),
#     "API_KEY": os.getenv("CLOUDINARY_API_KEY", ""),
#     "API_SECRET": os.getenv("CLOUDINARY_API_SECRET", ""),
# }

# # FAIL SAFE CHECK (THIS PREVENTS 500 CRASH)
# if not all([
#     CLOUDINARY_STORAGE["CLOUD_NAME"],
#     CLOUDINARY_STORAGE["API_KEY"],
#     CLOUDINARY_STORAGE["API_SECRET"],
# ]):
#     print("⚠️ WARNING: Cloudinary env vars missing!")

#DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ========================
# CKEDITOR
# ========================

DJANGO_CKEDITOR_5_UPLOAD_FILE_VIEW = "django_ckeditor_5.views.upload_file"
DJANGO_CKEDITOR_5_UPLOAD_IMAGE_VIEW = "django_ckeditor_5.views.upload_image"

CKEDITOR_5_CONFIGS = {
    "default": {
        "toolbar": [
            "heading", "|",
            "bold", "italic", "underline", "|",
            "link", "bulletedList", "numberedList", "|",
            "blockQuote", "imageUpload", "|",
            "undo", "redo"
        ],
        "height": 500,
        "width": "100%",
    }
}

# ========================
# SECURITY FIX
# ========================

X_FRAME_OPTIONS = "SAMEORIGIN"
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

SECURE_SSL_REDIRECT = not DEBUG
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG

# ========================
# DEFAULT PK
# ========================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'