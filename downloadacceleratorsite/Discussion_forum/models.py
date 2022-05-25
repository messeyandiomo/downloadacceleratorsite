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

#child of model Forum
class Question(models.Model):
    forum = models.ForeignKey(Forum,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=1000, blank=False, default="")
    details = models.TextField(blank=False, null=False, default="")

    def __str__(self):
        return str(self.forum)

#child of model Question
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(blank=False, null=False, default="")

    def __str__(self):
        return str(self.question)