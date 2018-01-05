from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celerydjango.settings')
 
app = Celery('celerydjango')
app.config_from_object('django.conf:settings', namespace='CELERY')
 
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-report-every-night': {
        'task': 'blog.tasks.send_view_count_report',
        'schedule': crontab(minute=0, hour=0), #if you want it to run daily at midnight
        # 'schedule': crontab(minute='*/1'), #if you want it to run at 5 min interval
    }
}

@app.task(bind=True)
def debug_task(self):
  print('Request: {0!r}'.format(self.request))
