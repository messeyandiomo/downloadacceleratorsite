from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request, 'downloadaccelerator/home.html')

def features(request):
    return render(request, 'downloadaccelerator/features.html')

def download(request):
    return render(request, 'downloadaccelerator/download.html')

def forums(request):
    return render(request, 'downloadaccelerator/forums.html')

def checkUser(request):
    if request.is_ajax and request.method == 'GET':
        username = request.GET.get("username", None)
        if User.objects.filter(username = username).exists():
            return JsonResponse({"valid": False}, status=200)
        else:
            return JsonResponse({"valid": True}, status=300)
    return JsonResponse({}, status=400)

def createUser(request):
    if request.is_ajax and request.method == 'GET':
        user = User.objects.create_user(username = request.GET.get("username"), email = request.GET.get("email"), password = request.GET.get("password"))
        if user is not None:
            return JsonResponse({"register": True}, status=200)
        else:
            return JsonResponse({"register": False}, status=300)
    return JsonResponse({}, status=400)

def userAuth(request):
    if request.is_ajax and request.method == 'POST':
        user = authenticate(username=request.POST['name'], password=request.POST['password'])
        if user is not None :
            return JsonResponse({"auth": True}, status=200)
        else:
            return JsonResponse({"auth": False}, status=200)
    return JsonResponse({}, status=200)
