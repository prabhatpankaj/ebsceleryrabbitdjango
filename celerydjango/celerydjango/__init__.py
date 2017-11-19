from __future__ import absolute_import, unicode_literals

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from celery import app as celery_app
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "celerydjango.settings")

# Add celery app defined in celery.py
__all__ = ['celery_app']