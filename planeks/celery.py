from __future__ import absolute_import, unicode_literals

import os 

from celery import Celery



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'planeks.settings')

app = Celery('planeks')

app.config_from_object('django.conf:settings', namespace='CELERY')


app.conf.update(BROKER_URL=os.environ['REDIS_URL'],
                CELERY_RESULT_BACKEND=os.environ['REDIS_URL'])

app.autodiscover_tasks()
