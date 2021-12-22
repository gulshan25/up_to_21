"""
Date and Time
---------------
date class
time class
datetime class
timedelta class

"""

# from datetime import  datetime,date
from datetime import *

dtobj=datetime.now()
print(dtobj)

dtobj2= date.today()
print(dtobj2)

print(dtobj.year)
print(dtobj.month)
print(dtobj.day)

print(dtobj.hour)
print(dtobj.minute)
print(dtobj.second)
print(dtobj.microsecond)

print(dtobj.strftime('Week Day short : %a'))
print(dtobj.strftime('Week Day long : %A'))
print(dtobj.strftime('Week Day number : %w'))

print(dtobj.strftime('Month short : %b'))
print(dtobj.strftime('Month long : %B'))
print(dtobj.strftime('Month number : %m'))

print(dtobj.strftime('Day of month : %d'))
print(dtobj.strftime('Year without century : %y'))
print(dtobj.strftime('Year with century : %Y'))

print(dtobj.strftime('Full time 0-23 : %T'))
print(dtobj.strftime('Full date  : %D'))


print(dtobj.strftime('Hour 0-23  : %H'))
print(dtobj.strftime('Hour 0-12  : %I'))
print(dtobj.strftime('AM:PM  : %p'))
print(dtobj.strftime('Minute  : %M'))
print(dtobj.strftime('Second  : %S'))
print(dtobj.strftime('Microsecond  : %f'))

print('display custom format: ')
print('-'*40)

#21-10-2021 
print(dtobj.strftime('%d-%m-%Y'))
print(dtobj.strftime('%d.%m.%Y'))
print(dtobj.strftime('%A, %d.%m.%Y'))


print(dtobj.strftime('%I:%M:%S %p'))
print(dtobj.strftime('%H:%M:%S '))





