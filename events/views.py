from django.shortcuts import render

# Create your views here.


#function base view for home 
def home(request):


	return render(request, 'events/home.html')


def details(request):


	return render(request, 'events/events_details.html')


def list(request):


	return render(request, 'events/event_list.html')




