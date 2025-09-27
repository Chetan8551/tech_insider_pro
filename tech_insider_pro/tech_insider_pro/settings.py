from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-qqy1+(-%4bv(chm_v&xrz4icls7pqyxi8!_dtp+y*asajes5hn'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mainapp',
    "django_ckeditor_5",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tech_insider_pro.urls'

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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

CKEDITOR_5_CONFIGS = {
    "default": {
        "toolbar": [
            "heading", "|",
            "fontSize", "fontFamily", "fontColor", "fontBackgroundColor", "|",
            "bold", "italic", "underline", "strikethrough", "highlight", "|",
            "alignment", "link", "|",
            "bulletedList", "numberedList", "todoList", "|",
            "blockQuote", "code", "codeBlock", "|",
            "insertTable", "imageUpload", "mediaEmbed", "horizontalLine", "|",
            "specialCharacters", "findAndReplace", "|",
            "undo", "redo", "removeFormat", "sourceEditing"
        ],
        "heading": {
            "options": [
                {"model": "paragraph", "title": "Paragraph", "class": "ck-heading_paragraph"},
                {"model": "heading1", "view": "h1", "title": "Heading 1", "class": "ck-heading_heading1"},
                {"model": "heading2", "view": "h2", "title": "Heading 2", "class": "ck-heading_heading2"},
                {"model": "heading3", "view": "h3", "title": "Heading 3", "class": "ck-heading_heading3"},
                {"model": "heading4", "view": "h4", "title": "Heading 4", "class": "ck-heading_heading4"},
            ]
        },
        "fontSize": {
            "options": [10, 12, 14, "default", 18, 20, 24, 30, 36, 48],
            "supportAllValues": True
        },
        "fontFamily": {
            "options": [
                "default",
                "Arial, Helvetica, sans-serif",
                "Courier New, Courier, monospace",
                "Georgia, serif",
                "Lucida Sans Unicode, Lucida Grande, sans-serif",
                "Tahoma, Geneva, sans-serif",
                "Times New Roman, Times, serif",
                "Trebuchet MS, Helvetica, sans-serif",
                "Verdana, Geneva, sans-serif"
            ]
        },
        "alignment": {
            "options": ["left", "center", "right", "justify"]
        },
        "image": {
            "toolbar": [
                "imageTextAlternative", "toggleImageCaption",
                "imageStyle:inline", "imageStyle:block", "imageStyle:side"
            ],
            "styles": ["inline", "block", "side"]
        },
        "table": {
            "contentToolbar": [
                "tableColumn", "tableRow", "mergeTableCells",
                "tableProperties", "tableCellProperties"
            ]
        },
        "mediaEmbed": {
            "previewsInData": True
        },
        "highlight": {
            "options": [
                {"model": "yellowMarker", "class": "marker-yellow", "title": "Yellow marker", "color": "var(--ck-highlight-marker-yellow)", "type": "marker"},
                {"model": "greenMarker", "class": "marker-green", "title": "Green marker", "color": "var(--ck-highlight-marker-green)", "type": "marker"},
                {"model": "pinkMarker", "class": "marker-pink", "title": "Pink marker", "color": "var(--ck-highlight-marker-pink)", "type": "marker"},
                {"model": "blueMarker", "class": "marker-blue", "title": "Blue marker", "color": "var(--ck-highlight-marker-blue)", "type": "marker"},
                {"model": "redPen", "class": "pen-red", "title": "Red pen", "color": "var(--ck-highlight-pen-red)", "type": "pen"},
                {"model": "greenPen", "class": "pen-green", "title": "Green pen", "color": "var(--ck-highlight-pen-green)", "type": "pen"}
            ]
        },
        "height": 500,
        "width": "100%"
    }
}




AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'mainapp' / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.DEBUG: 'debug',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DJANGO_CKEDITOR_5_UPLOAD_FILE_VIEW = "django_ckeditor_5.views.upload_file"
DJANGO_CKEDITOR_5_UPLOAD_IMAGE_VIEW = "django_ckeditor_5.views.upload_image"
