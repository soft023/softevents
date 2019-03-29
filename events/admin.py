from django.contrib import admin
from .models import Event,Category,State,Booking, Feedback
# Register your models here.



admin.site.register(Event)
admin.site.register(State)
admin.site.register(Category)
admin.site.register(Booking)
admin.site.register(Feedback)