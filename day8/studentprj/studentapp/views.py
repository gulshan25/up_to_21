from django.shortcuts import render
from studentapp.models import Student
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    context ={'title':'hello'}
    return render(request,'stud/home.html',context)

def list(request):
    students = Student.objects.order_by('-id')
    std_list = std
    paginator = Paginator(std_list,5)
    page = request.GET.get('page')
    
    context = {'title':'Student List','students':students}
    return render(request,'stud/list.html',context)

def about(request):
    context = {'title': 'About'}
     return render(request,'stud/list.html',context)