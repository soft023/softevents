from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Category(models.Model):

	name = models.CharField(max_length=15)
	categorypic = models.ImageField(default='default.jpg', upload_to='category_pics',null=True)
	addedby = models.ForeignKey(User,null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.name


class State(models.Model):

	name = models.CharField(max_length=15)

	def __str__(self):
		return self.name




class Event(models.Model):

	title = models.CharField(max_length=100)
	category = models.ForeignKey(Category,null=True, on_delete=models.SET_NULL)
	state  = models.ForeignKey(State,null=True, on_delete=models.SET_NULL)
	price = models.DecimalField(max_digits=6, decimal_places=2,null=True)
	venue = models.TextField()
	reservation = models.CharField(max_length=10,null=True)
	reserved = models.CharField(max_length=10,null=True)
	statedate = models.DateTimeField(null=True)
	enddate = models.DateTimeField(null=True)
	starttime = models.TimeField(null=True)
	endtime = models.TimeField(null=True)
	rating = models.CharField(max_length=10,null=True)
	organisername = models.CharField(max_length=30,null=True)
	organiseremail = models.CharField(max_length=100,null=True)
	organiserphone = models.CharField(max_length=12,null=True)
	banner1 = models.ImageField(default='default.jpg', upload_to='banners',null=True)
	banner2 = models.ImageField(default='default.jpg', upload_to='banners',null=True)
	speaker1name = models.CharField(max_length=30,null=True)
	speaker2name = models.CharField(max_length=30,null=True)
	speaker1bio	= models.TextField(null=True)
	speaker2bio = models.TextField(null=True)
	speaker1pics = models.ImageField(default='default.jpg', upload_to='speaker_pics',null=True)
	speaker2pics = models.ImageField(default='default.jpg', upload_to='speaker_pics',null=True)
	tags = models.CharField(max_length=50,null=True)
	description1 = models.TextField(null=True)
	description2 = models.TextField(null=True) 
	moreinfo = models.TextField(null=True)
	postedby = models.ForeignKey(User,null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.title

		#this is use redirect after creating new post
	#def get_absolute_url(self):
	#	return reverse('', kwargs={'pk' :self.pk})



class Booking(models.Model):

	eventid = models.ForeignKey(Event,null=True, on_delete=models.SET_NULL)
	participantid = models.ForeignKey(User,null=True, on_delete=models.SET_NULL)
	bookingid = models.CharField(max_length=10)
	date = models.DateTimeField(null=True)

	def __str__(self):
		return self.bookingid


class Feedback(models.Model):

	eventid = models.ForeignKey(Event,null=True, on_delete=models.SET_NULL)
	participantid = models.ForeignKey(User,null=True, on_delete=models.SET_NULL)
	comment = models.TextField()
	date = models.DateTimeField(null=True)

	def __str__(self):
		return self.id