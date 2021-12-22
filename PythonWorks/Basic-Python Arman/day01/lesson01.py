'''
author:Arman Hossen
Lesson1: Variable
date: 21 sept 21

'''
print('hello world')
name='arman hossen'
age=12
salary=2000.00
print(name)
print(age)
print(salary)

# display variable datatype 
print(type(name))
print(type(age))
print(type(salary))
print(name,age,salary)

print('Name:'+name+'\tAge:'+str (age)+'\tSalary:'+str (salary))
print('Name:'+name+'\nAge:'+str (age)+'\nSalary:'+str (salary))


print('Name:{0} \nAge:{1} \nSalary:{2} \n'.format(name,age,salary))

print('Name:{} \nAge:{} \nSalary:{} \n'.format(name,age,salary))

print(f'Name:{name} \nAge:{age} \nSalary:{salary} \n')

print('Name:%s \nAge:%s \nSalary:%s \n'%(name,age,salary))

