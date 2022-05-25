from django.forms import ModelForm
from .models import *

class CreateInForum(ModelForm):
    class Meta:
        model= Forum
        fields = "__all__"

class CreateInQuestion(ModelForm):
    class Meta:
        model= Question
        fields = "__all__"

class CreateInAnswer(ModelForm):
    class Meta:
        model= Answer
        fields = "__all__"