from unicodedata import name
from django.shortcuts import render,redirect
from .models import * 
from .forms import * 
from django.http import JsonResponse

# Create your views here.

def home(request):
    forums=forum.objects.all()
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

def addInDiscussion(request):
    form = CreateInDiscussion()
    if request.method == 'POST':
        form = CreateInDiscussion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={'form':form}
    return render(request,'Discussion_forum/addInDiscussion.html',context)


def getForums(request):
    forumsList = []
    if request.is_ajax and request.method == 'GET':
        forums=forum.objects.all()
        if forums is not None:
            for f in forums :
                forumsList.append(f.name)
            return JsonResponse({"exist": True, "forumsList": forumsList}, status=200)
        else:
            return JsonResponse({"exist": False}, status=300)