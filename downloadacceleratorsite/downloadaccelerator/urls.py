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
    path('userlogout', views.logOutUser, name='logoutuser'),
    path('checkusermail', views.checkUserMail, name='checkUserMail'),
    path('passwordreset', views.passwordReset, name='passwordreset'),
]
