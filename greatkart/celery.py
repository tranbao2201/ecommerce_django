from __future__ import absolute_import, unicode_literals

import os
from re import A
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'greatkart.settings')
app = Celery('greatkart')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()