from django.shortcuts import render
from django.views.generic import *
from empapp.models import Employee

# Create your views here.

class HomeView(TemplateView):
    template_name = 'emp/home.html'
    
class EmployeeListView(ListView):
    model = Employee
    template_name = 'emp/list.html'
    paginate_by = 5
    queryset = Employee.objects.order_by('-id')
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Employee List"
        return context    