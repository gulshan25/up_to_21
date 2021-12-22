'''
# A class is a blueprint for the object
# An object has 2 characteristics
# A.Attributes
# B.Behavior

class ClassName(object):
    --snip-- 

making an instances/object from a class 
objectName=ClassName(arguments)
'''
class Calculator(object):
    def addition (self,x,y):
        return x+y

    

    def subtraction (self,x,y):
        return x-y     

    def multiplication (self,x,y):
        return x*y

    def divition (self,x,y):
        return x/y    





C1= Calculator()
print(C1.addition(20,30))
print(C1.subtraction(20,30))
print(C1.multiplication(20,30))
print(C1.divition(20,30))



   
