from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'downloadaccelerator/home.html')

def features(request):
    return render(request, 'downloadaccelerator/features.html')