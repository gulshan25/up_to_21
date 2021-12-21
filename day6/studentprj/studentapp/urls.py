from django.urls import path
from studentapp import views


urlpatterns = [
    path('list/', views.list,name = 'list')
    
]
