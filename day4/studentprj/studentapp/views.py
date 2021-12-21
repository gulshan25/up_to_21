from django.shortcuts import render

# Create your views here.

def home(request):
    context={'title':'Amar django shikhte hobei'}
    return render(request,'stud/home.html',context)