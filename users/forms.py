from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profilepics



class UserRegistrationForm(UserCreationForm):
		
	email = forms.EmailField()

	class Meta:
		model =User
		fields = ['first_name','last_name','username','email','password1','password2']






#for user Update form

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model =User
		fields = ['first_name','last_name','username','email']




# This is to update the profile picture as well
class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model =Profilepics
		fields = ['image']
	