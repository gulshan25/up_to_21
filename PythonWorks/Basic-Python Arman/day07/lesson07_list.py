'''
List
-------
listvar=[]

'''

motorcycles=['Honda','Yamaha','Suzuki']
print(motorcycles)
# print(motorcycles[0])
# print(motorcycles[1])
# print(motorcycles[2])

for motor in motorcycles :
    print(motor)

i=0
while i<2 :
    print(motorcycles[i])
    i+=1

'''
change
--------

'''   

motorcycles[1]='Hero'
print(motorcycles)

motorcycles.append('Bazaz')
print(motorcycles)
motorcycles.insert(2,'Yamaha')
print(motorcycles)

fruits=[]
fruits.append('Mango')
fruits.append('Orange')
fruits.append('Banana')
fruits.append('Grape')
fruits.append('Lichi')
print(fruits)
fruits.insert(4,'Jackfruit')
print(fruits)

fruits.extend(['Mango','Bangi','Dragonfruit','Watermelon','Grape','Apple'])
print(fruits)

# delete using index

del fruits[7]
print(fruits)

#delete using item name

fruits.remove('Dragonfruit')
print(fruits)

fruits.pop() # LIFO 
fruits.pop() # LIFO 
print(fruits)
print(dir(fruits))

print(fruits.count('Mango'))
print(fruits.index('Mango'))
print(fruits.index('Grape'))

fruits.reverse()
print(fruits)

fruits.sort()
print(fruits)

fruits.sort(reverse=True)
print(fruits)

print(f'Total number of fruits:{len(fruits)}')

# slicing list
print(fruits[-1])
print(fruits[-2])
print(fruits[-3])
print(fruits[0:3])
print(fruits[2:5])
print(fruits[3:])
print(fruits[:4])






















