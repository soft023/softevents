from django.shortcuts import render

# Create your views here.


#function base view for home 
def home(request):


	return render(request, 'events/home.html')
