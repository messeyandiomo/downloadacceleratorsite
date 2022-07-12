from django.shortcuts import render



# Create your views here.

def home(request):
    context = {}
    if request.method == 'GET':
        if request.user.is_authenticated:
            username = request.user.get_username()
            if username is not None :
                context = {'username': username}
    if len(context) != 0:
        return render(request, 'downloadaccelerator/home.html', context)
    else:
        return render(request, 'downloadaccelerator/home.html')



def features(request):
    context = {}
    if request.method == 'GET':
        if request.user.is_authenticated:
            username = request.user.get_username()
            if username is not None :
                context = {'username': username}
    if len(context) != 0:
        return render(request, 'downloadaccelerator/features.html', context)
    else:
        return render(request, 'downloadaccelerator/features.html')



def download(request):
    context = {}
    if request.method == 'GET':
        if request.user.is_authenticated:
            username = request.user.get_username()
            if username is not None :
                context = {'username': username}
    if len(context) != 0:
        return render(request, 'downloadaccelerator/download.html', context)
    else:
        return render(request, 'downloadaccelerator/download.html')


def aboutauthor(request):
    context = {}
    if request.method == 'GET':
        if request.user.is_authenticated:
            username = request.user.get_username()
            if username is not None :
                context = {'username': username}
    if len(context) != 0:
        return render(request, 'downloadaccelerator/aboutauthor.html', context)
    else:
        return render(request, 'downloadaccelerator/aboutauthor.html')
                


