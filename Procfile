release: python manage.py migrate --no-input
web: gunicorn planeks.wsgi
worker: celery -A planeks.celery worker -B --loglevel=info
