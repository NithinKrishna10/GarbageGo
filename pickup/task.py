# tasks.py
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from apscheduler.schedulers.background import BackgroundScheduler
from .models import PickupTracker
from datetime import datetime

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")

def reset_pickup_tracker():
    current_month = datetime.now().month
    PickupTracker.objects.all().update(scrap_weight=0, waste_weight=0)

scheduler.add_job(reset_pickup_tracker, "cron", month="*", day=1, hour=0, minute=0, id="reset_pickup_tracker")

scheduler.start()
