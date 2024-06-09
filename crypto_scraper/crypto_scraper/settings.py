# crypto_scraper/settings.py

INSTALLED_APPS = [
    
    'rest_framework',
    'scraper',
    'django_celery_results',
]

# Celery Configuration
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# crypto_scraper/settings.py

ROOT_URLCONF = 'crypto_scraper.urls'
