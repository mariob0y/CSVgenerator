web: gunicorn planeks.wsgi
worker: celery -A dummy_gen.tasks worker -B --loglevel=info
