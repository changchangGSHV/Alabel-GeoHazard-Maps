from django.urls import path
from . import views

urlpatterns = [
    path('',views.flood.as_view(),name='flood'),
]
