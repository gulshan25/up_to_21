'''
Tuple
------
tuplename=(value1,value2,value3,....)



'''

magicians=('Sajib','Sujon','Sabyassachi','Sayeda')
print(magicians)

for x in magicians :
    print(x)

digits= (12,10,34,67,45,37,89,90,13,16,65)
print(digits)
print(max(digits))
print(min(digits))
print(sum(digits))

players=('Mohammad Ali','Arman','Shuvo','Gulshan','Arina','Maruf')
print(players [0:3])

actors=players[:]
print(actors)

print(dir(actors))

print(actors.index('Gulshan'))
print(actors.count('Gulshan'))




