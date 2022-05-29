from unicodedata import name
from django.shortcuts import render,redirect
from .models import * 
from .forms import * 
from django.http import JsonResponse

# Create your views here.

def home(request):
    forums=Forum.objects.all()
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request,'Discussion_forum/home.html',context)

def addInForum(request):
    form = CreateInForum()
    if request.method == 'POST':
        form = CreateInForum(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={'form':form}
    return render(request,'Discussion_forum/addInForum.html',context)

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
    if request.method == 'GET':
        username = request.GET.get("username", None)
        if username is not None :
            context = {'username': username}
    if forumName is not None:
        context['forumName'] = forumName
        if discussionId is not None:
            discussion = Question.objects.get(id=discussionId)
            context["discussion"] = {"id": discussionId, "creator": discussion.user, "topic": discussion.topic, "details": discussion.details}
            answersList = []
            answers = Answer.objects.filter(question=discussion)
            if answers is not None:
                for a in answers:
                    answersList.append({"poster": a.user, "message": a.message})
                context["answersList"] = answersList
        else:
            questionsList = []
            questions = Question.objects.filter(forum=Forum.objects.filter(name=forumName).get().id)
            if questions is not None:
                for q in questions:
                    questionsList.append({"id": q.id, "forumname": forumName, "username": q.user, "topic": q.topic, "details": q.details})
                context["questionsList"] = questionsList
    else:
        forumsList = []
        forums = Forum.objects.all()
        if forums is not None:
            for f in forums:
                forumsList.append({"name": f.name, "title": f.title, "description": f.description})
            context["forumsList"] = forumsList
    return render(request, 'Discussion_forum/forums.html', context)