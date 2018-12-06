from django.shortcuts import render
from django.urls import reverse_lazy

from geopy.geocoders import Nominatim
from geopy.distance import geodesic, great_circle

from django.views import generic 

from .models import Job
#from django.conf import settings 

#APP_LOCATION = settings.DEFAULT_LOCATION

class HomeView(generic.TemplateView):
	template_name = 'home.html'


class JobView(generic.DetailView):
	model = Job
	template_name = 'job.html'
	

class JobListView(generic.ListView):
	model = Job
	template_name = 'job_list.html'
	
class JobSearchView(generic.ListView):
	model = Job
	template_name = 'job_search.html'
	
	def get_context_data(self, **kwargs):
		geolocator = Nominatim(user_agent="Geopy Test")
		context = super(JobSearchView, self).get_context_data(**kwargs)
		s_Loc = 35.593553, -105.221299
		close_jobs = []
		for job in Job.objects.all():
			end = geolocator.geocode(job.address)
			e_Loc = end.latitude, end.longitude
			GD = geodesic(s_Loc, e_Loc).miles
			if GD <= 100:
				close_jobs.append(job)
				
		context['close_jobs'] = close_jobs
		return context