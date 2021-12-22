'''
Demonstrate sets
------------------
variable=set(['a','b','c'])

HW ===> 1+1=3 called fibonacci numbers  
'''

# myset={'p','q','r'}
myset=set(['a','b','c'])
print(myset)
myset.add('d')
print(myset)
print(dir(myset))

people={'Maruf','Arman','Sajib'}
vampire={'Gulshan','Arina','Tania'}
dracula={'Shuvo','Shujon','Halder'}

population1= people.union(vampire)
print(population1)
population2= people| vampire
print(population2)

set1=set()
set2=set()
for i in range(5) :
    set1.add(i)
for i in range(3,9):
    set2.add(i)

print(set1)
print(set2)

set3=set1.intersection(set2)
print(set3)

set4=set1 & set2
print(set4)



