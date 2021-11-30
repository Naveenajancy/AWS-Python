from __future__ import absolute_import
from celery import Celery
import os

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "sqs_quickstart.settings")
# argument to Celery is name of the current module
app = Celery('sqs_quickstart')
# Loads configuration from a configuration object
app.config_from_object('django.conf:settings')
print("calling autodiscover task")
app.autodiscover_tasks()
