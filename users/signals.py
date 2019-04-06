#all these signal.py is for auto inserting into another which has one on one relationship with this user table
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profilepics




@receiver(post_save, sender=User)
def create_profilepics(sender, instance, created, **kwargs):
	if created:
		Profilepics.objects.create(user=instance)




@receiver(post_save, sender=User)
def save_profilepics(sender, instance, **kwargs):
	instance.profilepics.save()