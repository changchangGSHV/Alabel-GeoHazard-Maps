from django.shortcuts import render
from .models import History, GeoHazard
from django.views.generic import ListView
from django.views import View
from itertools import chain






class history(ListView):
	model = GeoHazard
	template_name = 'auxiliary/geohazard_history.html'
	context_object_name = 'geohazards'
	# paginate_by = 1

	# def get_context_data(self, **kwargs):
	# 	context = super(history, self).get_context_data(**kwargs)
	# 	context['histories'] = History.objects.all()
	# 	context['geohazards'] = GeoHazard.objects.all()
	# 	return context























# class history(ListView):
# 	model = GeoHazard
# 	template_name = 'auxiliary/geohazard_history.html'
# 	paginate_by = 1

# 	def get_context_data(self, **kwargs):
# 		context = super(history, self).get_context_data(**kwargs)
# 		context['histories'] = History.objects.all()
# 		context['geohazards'] = GeoHazard.objects.all()
# 		return context