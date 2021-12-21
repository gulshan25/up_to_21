from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def myfunc1(request):
    return HttpResponse('Hello, My Dear friend Tania ')

def welcome(request,name):
    return HttpResponse(f'Hello my Dear friend {name}')

def show(request):
    context = {'title':'welcome'}
    return render(request,'home.html',context)
