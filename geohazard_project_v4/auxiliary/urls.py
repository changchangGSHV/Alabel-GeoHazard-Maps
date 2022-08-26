from django.urls import path
from . import views

urlpatterns = [
	path('',views.HomeTemplateView.as_view(),name='home'),
	path('history/',views.HistoryListView.as_view(),name='history'),
	path('contacts/',views.ContactTemplateView.as_view(),name='contacts'),

]