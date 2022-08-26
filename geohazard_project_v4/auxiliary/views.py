from django.shortcuts import render
from .models import History, GeoHazard, Assessment, Contacts, Hotlines
from django.views.generic import ListView, TemplateView



class HomeTemplateView(TemplateView):
   template_name = 'auxiliary/home.html'


class ContactTemplateView(TemplateView):
   model = Contacts
   context_object_name = 'contacts'
   template_name = 'auxiliary/contacts.html'

   def get_context_data(self, **kwargs):
      context = super(ContactTemplateView, self).get_context_data(**kwargs)
      context.update({
         'mdrrm_office': Hotlines.objects.filter(contacts_id=1),
         'alabel_info_office': Hotlines.objects.filter(contacts_id=2)
      })

      return context


class HistoryListView(ListView):
   model = History
   template_name = 'auxiliary/history.html'
   context_object_name = 'histories'
   paginate_by = 1

   def get_queryset(self):
       histories = super().get_queryset()
       histories = histories.prefetch_related("geohazards", "assessment")
       return histories

