# signals.py

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PickupTracker

@receiver(post_save, sender=User)
def create_pickup_tracker(sender, instance, created, **kwargs):
    if created:
        PickupTracker.objects.create(user=instance)
