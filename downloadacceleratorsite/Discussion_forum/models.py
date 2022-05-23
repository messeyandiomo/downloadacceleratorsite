from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
    
#parent model
class Forum(models.Model):
    name=models.CharField(max_length=200, unique=True, blank=False)
    title= models.CharField(max_length=300)
    description = models.CharField(max_length=1000,blank=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return str(self.title)

#child model
class Discussion(models.Model):
    forum = models.ForeignKey(Forum,blank=True,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=1000, unique=True, blank=False, default="topic of the discussion")
    postedmessage = models.TextField(blank=False, null=False, default="write your message here")

    def __str__(self):
        return str(self.forum)