from django.core import paginator
from django.shortcuts import redirect, render 
from studentapp.forms import StudentForm, SignUpForm
from studentapp.models import Student
from django.core.paginator import Paginator
from django.contrib import messages


# Create your views here.

def home(request):
    context = {'title':'Home'}
    return render(request,'stud/home.html',context)

def list(request):
    # students = Student.objects.all()
    std = Student.objects.order_by('-id')
    stdlist = std
    paginator = Paginator(stdlist,5)
    page = request.GET.get('page')
    std = paginator.get_page(page)
    
    context = {'title':'Student List','students': std}
    return render(request,'stud/list.html',context)

def about(request):
    context = {'title':'About Us'}
    return render(request,'stud/about.html',context)

def create(request):
    # POST = when submit 
    # GET = before submit 
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Data inserted successfully')
            return redirect('list')
    else:
        form = StudentForm()
    context = {'title': 'Create Student','form':form}
    return render(request,'stud/create.html',context)

def details(request, id):
    student = Student.objects.get(pk = id)
    form = StudentForm(request.POST or None, instance=student)
    
    context = {'title': 'Student Details','form':form, 'student':student}
    return render(request,'stud/view.html',context)
    
def edit(request, id):
    if request.method == "POST":
      student = Student.objects.get(pk = id)
      form = StudentForm(request.POST or None, instance=student)
      if form.is_valid():
          form.save()
          messages.success(request,'Data Updated successfully')
          return redirect('list')
    else:
        student = Student.objects.get(pk = id)
        form = StudentForm(request.POST or None, instance=student)
        
    context = {'title': 'Edit Student','form':form}
    return render(request,'stud/create.html',context)    

def delete(request, id):
    
    student = Student.objects.get(pk = id)
    student.delete()
    messages.success(request,'Data deleted successfully')
    return redirect('list')

def register(request):
    
     if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                user.save()
                messages.success(request,'User created successfully')
                return redirect('home')
   
     else:
         form = SignUpForm()       
     context = {'title': 'Register User','form':form}
     return render(request,'registration/register.html',context)

        
    


