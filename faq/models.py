from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Frequentquestions(models.Model):

	question = models.TextField(null=True) 
	answer = models.TextField(null=True) 
	addedby = models.ForeignKey(User,null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.question