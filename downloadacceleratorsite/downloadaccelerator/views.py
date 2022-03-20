from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request, 'downloadaccelerator/home.html')

def features(request):
    return render(request, 'downloadaccelerator/features.html')

def download(request):
    return render(request, 'downloadaccelerator/download.html')

def checkUser(request):
    if request.is_ajax and request.method == 'GET':
        username = request.GET.get("username", None)
        if User.objects.filter(username = username).exists():
            return JsonResponse({"valid": False}, status=200)
        else:
            return JsonResponse({"valid": True}, status=300)
    return JsonResponse({}, status=400)