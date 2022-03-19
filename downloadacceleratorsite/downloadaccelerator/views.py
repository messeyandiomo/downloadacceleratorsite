from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request, 'downloadaccelerator/home.html')

def features(request):
    return render(request, 'downloadaccelerator/features.html')

def download(request):
    return render(request, 'downloadaccelerator/download.html')

def checkUser(request, username):
    return User.objects.filter(username=username).exists()