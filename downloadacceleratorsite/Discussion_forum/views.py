from unicodedata import name
from django.shortcuts import render,redirect
from .models import * 
from .forms import * 
from django.http import JsonResponse

# Create your views here.

def home(request):
    return render(request,'Discussion_forum/home.html')

def forth(request):
    return render(request,'Discussion_forum/forward.html')

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
    if request.is_ajax and request.method == 'GET':
        if request.user.is_authenticated:
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
                context["count"] = len(answersList)
        else:
            questionsList = []
            questions = Question.objects.filter(forum=Forum.objects.filter(name=forumName).get().id)
            totalPosts = 0
            if questions is not None:
                for q in questions:
                    numberOfPosts = q.answer_set.all().count() + 1
                    questionsList.append({"id": q.id, "forumname": forumName, "username": q.user, "topic": q.topic, "details": q.details, "numberOfPosts": numberOfPosts})
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
                forumsList.append({"name": f.name, "title": f.title, "description": f.description, "numberOfTopics": numberOfTopics, "numberOfPosts": numberOfPosts})
                totalPosts = totalPosts + numberOfPosts
            context["forumsList"] = forumsList
            context["count"] = totalPosts
    return render(request, 'Discussion_forum/forums.html', context)