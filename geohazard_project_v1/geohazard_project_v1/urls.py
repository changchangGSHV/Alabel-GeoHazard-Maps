"""geohazard_project_v1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from landslide import views as landslide_views
from django.conf import settings
from django.conf.urls.static import static
from auxiliary import views as auxiliary_views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('flood.urls')),
    path('landslide/', landslide_views.landslide.as_view(),name='landslide'),
    path('history/',auxiliary_views.history.as_view(),name='history'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)