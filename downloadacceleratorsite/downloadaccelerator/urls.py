from xml.etree.ElementInclude import include
from django.urls import path

from . import views

app_name = 'downloadaccelerator'
urlpatterns = [
    path('', views.home, name='home'),
    path('home.html', views.home, name='home'),
    path('features.html', views.features, name='features'),
    path('download.html', views.download, name='download'),
    path('username', views.checkUser, name='user'),
]