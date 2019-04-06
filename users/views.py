from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm	
from django.contrib.auth.decorators import login_required #this is to set something like middleware/guard 

# Create your views here.




def register(request):

	if request.method == 'POST':
	 form = UserRegistrationForm(request.POST)
	 if form.is_valid():
	 	username = form.cleaned_data.get('username')
	 	first_name= form.cleaned_data.get('first_name')
	 	last_name = form.cleaned_data.get('last_name')
	 	form.save()
	 	messages.success(request,f'Your account has been created ! You can now Log in ')
	 	return redirect('login')
	else:
		form = UserRegistrationForm()
	return render(request,'users/register.html',{'form': form})





def aboutus(request):


	return render(request, 'users/aboutus.html')


#@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profilepics.image)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request,f'Your account has been Updated ')
			return redirect('profile')


	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profilepics)
	
	context = {
	'u_form': u_form,
	'p_form': p_form
	}
	return render(request,'users/profile.html', context)
