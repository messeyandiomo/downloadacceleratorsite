from django.urls import path

from . import views

app_name = 'downloadaccelerator'
urlpatterns = [
    path('', views.home, name='home'),
    path('features.html', views.features, name='features'),
    path('download', views.download, name='download'),
    path('modalconnexion/', views.modalconnexion, name='modalconnexion'),
    path('modalconnexion/<str:modaltype>', views.modalconnexion, name='modalconnexion'),
    path('modalwelcome/', views.modalwelcome, name='modalwelcome'),
    path('modalwelcome/<str:username>', views.modalwelcome, name='modalwelcome'),
    path('username', views.checkUser, name='user'),
    path('createuser', views.createUser, name='createuser'),
    path('userauth', views.userAuth, name='userauth'),
    path('checkusermail', views.checkUserMail, name='checkUserMail'),
    path('passwordreset', views.passwordReset, name='passwordreset'),
    path('forums/', views.forums, name='forums'),
    path('forums/<str:forumName>', views.forums, name='forums'),
]
