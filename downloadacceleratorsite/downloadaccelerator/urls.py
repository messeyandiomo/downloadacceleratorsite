from django.urls import path

from . import views

app_name = 'downloadaccelerator'
urlpatterns = [
    path('', views.home, name='home'),
    path('features.html', views.features, name='features'),
    path('download', views.download, name='download'),
    path('username', views.checkUser, name='user'),
    path('createuser', views.createUser, name='createuser'),
    path('userauth', views.userAuth, name='userauth'),
    path('<str:forumName>', views.forums, name='forums'),
]
