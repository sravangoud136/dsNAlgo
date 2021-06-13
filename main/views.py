from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_sameorigin
from main import models

# Create your views here.
def index(request):
    return HttpResponse('test')
def showproblems(request):
    p=models.Problem.objects.all()
    t=models.Tag.objects.all()
    context={
        "problems":p,
        "tags":t
    }
    return render(request,'index.html',context)
@xframe_options_sameorigin
def problemswithtag(request,tag):
    t=models.Tag.objects.filter(tag=tag)
    print(t)
    problems=[]
    for i in t[0].problem_set.all():
        problems.append(i)
    context={
        "problems":problems,
        "tag":tag
    }
    return render(request,"problems-list.html",context)
@xframe_options_sameorigin
def viewproblem(request,pk):
    p=models.Problem.objects.filter(pk=pk)
    context={
        "problem":p
    }
    return render(request,"problem-view.html",context)