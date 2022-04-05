from django.urls import path
from Discussion_forum.views import *

app_name = 'Discussion_forum' 
urlpatterns = [
    path('',home,name='home'),
    path('addInForum/',addInForum,name='addInForum'),
    path('addInDiscussion/',addInDiscussion,name='addInDiscussion'),
]