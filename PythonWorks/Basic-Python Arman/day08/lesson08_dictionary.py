'''
dictionary
--------------
variable={'key':value}

HW = 10 person info

'''
person1={'Id':1,'Name':'Hasibur Hossain Arman','Phone':'+8801545465677'}

print(person1)
print(person1['Id'])
print(person1['Name'])
print(person1['Phone'])

person2=person1.copy()
print(person2)
# use a update method
person2.update({'Name':'Sujon Raaj Bongshi'})
person2.update({'Age': 16})
print(person2)
# delete by key
del person2['Age']
print(person2)

print(type(person2))
print(dir(person2))

person2.clear()
print(person2)

print(person1.items())
print(list(person1.items()))
print('Display only keys:')
print(person1.keys())
for k in person1.keys() :
    print(k)

print(person1.values())

for v in person1.values():
    print(v)


for key in person1.keys() :
    print(f'{key}={person1[key]}')


personkey=list(person1.keys())
print(personkey)
personkey.sort()
print(personkey)
personkey.sort(reverse=True)
print(personkey)

for key in personkey :
    print(f'{key}={person1[key]}')

students={}
students['Id']=1
students['Name']='Sabyasachi Haldiram'
students['Age']=12
print(students)
print(students.get('Name'))
print(students.get('Phone'))
print(students.get('Phone','No phone found'))
# print(students['phone'])




















