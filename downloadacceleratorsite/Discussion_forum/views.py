from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .models import * 
from .forms import * 
from django.http import JsonResponse

from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.core.mail import send_mail

# Create your views here.

def loginUser(request):
    return render(request,'Discussion_forum/login.html')


def logoutUser(request):
    if request.is_ajax and request.method == 'GET':
        if request.user.is_authenticated:
            logout(request)
    return render(request, 'Discussion_forum/logout.html')

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

def addInQuestion(request):
    if request.is_ajax and request.method == 'POST':
        question = Question.objects.create(forum=Forum.objects.filter(name=request.POST["forumname"]).get(), user=User.objects.filter(username=request.POST["username"]).get(), topic=request.POST["topic"], details=request.POST["details"])
        if question is not None:
            return JsonResponse({"added": True}, status=200)
        else:
            return JsonResponse({"added": False}, status=200)
    return JsonResponse({}, status=200)

def addInAnswer(request):
    if request.is_ajax and request.method == 'POST':
        answer = Answer.objects.create(question=Question.objects.get(id=request.POST["questionid"]), user=User.objects.get(username=request.POST["username"]), message=request.POST["message"])
        if answer is not None:
            return JsonResponse({"added": True}, status=200)
        else:
            return JsonResponse({"added": False}, status=200)
    return JsonResponse({}, status=200)

def getForums(request):
    forumsList = []
    if request.is_ajax and request.method == 'GET':
        forums=Forum.objects.all()
        if forums is not None:
            for f in forums :
                forumsList.append({"name": f.name, "title": f.title})
            return JsonResponse({"exist": True, "forumsList": forumsList}, status=200)
        else:
            return JsonResponse({"exist": False}, status=300)


def forums(request, forumName=None, discussionId=None):
    context = {}
    if request.is_ajax and request.method == 'GET':
        if request.user.is_authenticated:
            username = request.user.get_username()
            if username is not None :
                context = {'username': username}
    if forumName is not None:
        context['forumName'] = forumName
        if discussionId is not None:
            discussion = Question.objects.get(id=discussionId)
            discussion.numberOfViews += 1
            discussion.save(update_fields=["numberOfViews"])
            context["discussion"] = {"id": discussionId, "creator": discussion.user, "topic": discussion.topic, "details": discussion.details}
            answersList = []
            answers = Answer.objects.filter(question=discussion).order_by("date_created")
            if answers is not None:
                for a in answers:
                    answersList.append({"date_created":a.date_created, "poster": a.user, "message": a.message})
                context["answersList"] = answersList
                context["count"] = len(answersList)
        else:
            forum = Forum.objects.get(name=forumName)
            forum.numberOfViews += 1
            forum.save(update_fields=["numberOfViews"])
            questionsList = []
            questions = Question.objects.filter(forum=Forum.objects.filter(name=forumName).get().id).order_by("date_created")
            totalPosts = 0
            if questions is not None:
                for q in questions:
                    numberOfPosts = q.answer_set.all().count() + 1
                    questionsList.append({"id": q.id, "forumname": forumName, "username": q.user, "date_created": q.date_created, "topic": q.topic, "details": q.details, "numberOfViews": q.numberOfViews, "numberOfPosts": numberOfPosts})
                    totalPosts = totalPosts + numberOfPosts
                context["questionsList"] = questionsList
                context["count"] = totalPosts
    else:
        forumsList = []
        forums = Forum.objects.all()
        if forums is not None:
            totalPosts = 0
            for f in forums:
                questions = f.question_set.all()
                numberOfTopics = questions.count()
                numberOfPosts = 0
                for q in questions:
                    numberOfPosts = numberOfPosts + q.answer_set.all().count() + 1
                forumsList.append({"name": f.name, "title": f.title, "description": f.description, "numberOfViews": f.numberOfViews, "numberOfTopics": numberOfTopics, "numberOfPosts": numberOfPosts})
                totalPosts = totalPosts + numberOfPosts
            context["forumsList"] = forumsList
            context["count"] = totalPosts
    return render(request, 'Discussion_forum/forums.html', context)