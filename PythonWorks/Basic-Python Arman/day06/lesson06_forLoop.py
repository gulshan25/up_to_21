'''
For loop
-----------
for variable  in collection: 
    statements


'''

from typing import Counter


data= list(range(5,20))
print(data)
x= list(range(20))
print(x)

y= list(range(1,11,3))
print(y)

for x in range(100) :
    print(x,end='\t')

print('\n')
print('-'*80)
for x in range(10,80+1):
    if x %2 ==0:
        print(x,end='\t')



print('\n')
print('-'*80)
for x in range(10,80+1):
    if x %2 != 0:
        print(x,end='\t')

print('\n')
print('-'*80)            



sum=0
for x in range(1,10+1):
    sum=sum+x
    print(x,end='+')

print('\b=',sum)

print('\n')
print('-'*80)


''' 
A-Z          =65-90
a-z          =96-122
back space   =8
space bar    =32

tab          =9
 0-9         =48-57


'''

for x in range(65,91) :
    print(chr(x),end='\t')
print('\n')


for x in range(97,123) :
    print(chr(x),end='\t')
print('\n')


c=input('Enter a character:')
print(f'The ASCII value of {c} is {ord(c)}' )
print('\n')


d= int(input('Enter a value:'))
print(f'The character of {d} is {chr(d)}' )
print('\n')