from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import JsonResponse

from django.contrib.auth.forms import PasswordResetForm
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.core.mail import send_mail



# Create your views here.
def home(request):
    return render(request, 'downloadaccelerator/home.html')

def features(request):
    return render(request, 'downloadaccelerator/features.html')

def download(request):
    return render(request, 'downloadaccelerator/download.html')


#def forums(request, forumName=None):
#    if forumName is not None:
#        return render(request, 'downloadaccelerator/forums.html', {'forumName': forumName})
#    else:
#        return render(request, 'downloadaccelerator/forums.html')


def forums(request, forumName=None):
    context = None
    if request.method == 'GET':
        username = request.GET.get("username", None)
        if username is not None :
            context = {'username': username}
    if forumName is not None:
        context['forumName'] = forumName
    if context is not None:
        return render(request, 'downloadaccelerator/forums.html', context)
    else:
        return render(request, 'downloadaccelerator/forums.html')
                

def checkUser(request):
    if request.is_ajax and request.method == 'GET':
        username = request.GET.get("username", None)
        if User.objects.filter(username = username).exists():
            return JsonResponse({"valid": False}, status=200)
        else:
            return JsonResponse({"valid": True}, status=300)
    return JsonResponse({}, status=400)


def checkUserMail(request):
    if request.is_ajax and request.method == 'GET':
        if User.objects.filter(username = request.GET.get("username"), email = request.GET.get("email")).exists():
            return JsonResponse({"valid": True}, status=200)
        else:
            return JsonResponse({"valid": False}, status=300)
    return JsonResponse({}, status=400)


def passwordReset(request):
    if request.is_ajax and request.method == "POST":
        user = User.objects.filter(username=request.POST["forgetName"], email=request.POST["forgetPassEmail"]).first()
        if user is not None:
            subject = "Password Reset Requested"
            email_template_name = "password/password_reset_email.html"
            c = {
                "email":user.email,
				'domain':'127.0.0.1:8000',
				'site_name': 'downloadaccelerator',
				"uid": urlsafe_base64_encode(force_bytes(user.pk)),
				"user": user,
				'token': default_token_generator.make_token(user),
				'protocol': 'http',
			}
            email = render_to_string(email_template_name, c)
            send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
            return JsonResponse({"reset": True}, status=200)
        else:
            return JsonResponse({"reset": False}, status=300)
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
            login(request, user)
            return JsonResponse({"auth": True}, status=200)
        else:
            return JsonResponse({"auth": False}, status=200)
    return JsonResponse({}, status=200)
