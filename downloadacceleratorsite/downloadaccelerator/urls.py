from django.urls import path

from . import views

app_name = 'downloadaccelerator'
urlpatterns = [
    path('', views.home, name='home'),
    path('features.html', views.features, name='features'),
    path('download', views.download, name='download'),
    path('aboutauthor', views.aboutauthor, name='aboutauthor'),
]
