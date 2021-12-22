'''
Polymorphism
===============================
	Polymorphism is an ability (in OOP) to use common interface for multiple form (data types).

'''

class Parrot:
    def fly(self):
        print('Parrot can fly')

    def swim (self):
        print('Parrot can not swim')


class Penguin:
    def fly(self):
        print('Penguin can not fly')

    def swim(self):
        print('Penguin can swim')


def Flying_Test(obj):
    obj.fly()

pr=Parrot()
pg=Penguin()

Flying_Test(pg)



            
    
        
