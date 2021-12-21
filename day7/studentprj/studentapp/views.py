from django.shortcuts import render
from studentapp.models import Student

# Create your views here.

def home(request):
    context ={'title':'hello'}
    return render(request,'stud/home.html',context)

def list(request):
    students = Student.objects.all()
    context = {'title':'Student List','students':students}
    return render(request,'stud/list.html',context)