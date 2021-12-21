import os
os.environ.setdefault()

import django
django.setup()

from studentapp.models import Student
///pip install faker///
from faker import Faker

fakezen = Faker()

def addstudent():
    fname = fakezen.name()
    femail = fakezen.email()
    fdob = fakezen.date()
    fmale = 'Male'
    
    std = Student.objects.get_or_create(name=fname, email=femail, dob=fdob, gender=fmale)