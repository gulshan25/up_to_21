from django.urls import path,include
from studentapp import views

urlpatterns = [
    path('home/', views.home,name='home'),
    path('list/', views.list,name='list'),
]
