import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'studentprj.settings')

import django
django.setup()

from studentapp.models import Student
from faker import Faker

fakezen = Faker()

def addstudent():
    fname = fakezen.name()
    femail = fakezen.email()
    fdob = fakezen.date()
    fmale = 'Male'
    
    std = Student.objects.get_or_create(name = fname,email = femail,dob = fdob,gender = fmale)[0]
    return std

def populatedata(n = 10):
    for x in range(n):
        std = addstudent()
        
if __name__=='__main__':
    print('populating data please wait...')
    print('#'*50)
    populatedata(30)
    print('populating data completed')
    print('#'*50)
    