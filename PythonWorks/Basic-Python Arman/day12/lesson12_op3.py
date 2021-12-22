'''
Inheritance
-------------
class BaseClass:
    body of BaseClass

class DerivedClass(BaseClass):
    body of DerivedClass 

{HW: Factorial 5! = 1*2*3*4*5= 120
    using loop only for HW}

'''

class Person:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age

    def walk (self):
        print(self.name.title()+' is now walking.')    

    def run(self):
        print(self.name.title()+' is now running.') 

    def show (self):
        s=self.name + ' '+str(self.age)
        # print(s)
        return s.title()

class Student(Person) :
    def __init__(self, name, age,fees) -> None:

        super().__init__(name, age)
        self.fees=fees

# polymorphism
    def show (self):
        s=self.name + ' '+str(self.age)+' fees:'+ str(self.fees)
        # print(s)
        return s.title()








#creating a instance of student class /object

stud1= Student ('sajib',12,12000)
stud1.run()
stud1.walk()

print(stud1.show())













            




        



