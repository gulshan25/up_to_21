'''
functions
-----------
def function_name(parameters):
    """ doc_string"""
    statements 

'''

def welcome():
    """This is a document srting """
    print('Hello Arman good morning')

welcome()
print(welcome.__doc__)

def welcome1(name):
    """This is a another document srting """
    print(f'Hello {name} good morning')

welcome1('Rajbongshi')
welcome1('Tania')

print(welcome1.__doc__)

def welcome2(name,msg):
    print(f'Hello {name} {msg}')
    
welcome2('Maruf','Good evening')
welcome2('ss','Good morning')

def welcome3(name1,name2,name3,name4):
    print(f'Hello {name1}')
    print(f'Hello {name2}')
    print(f'Hello {name3}')
    print(f'Hello {name4}')

welcome3('Sajib','Gulshan','Banani','Arman')


#Python Arbitrary Arguments
def welcome4(*name):
    for x in name:    
        print(f'Hello {x}')

#calling function 

welcome4('Sajib','Gulshan','Banani','Arman','Shuvo','Nazmul')

def welcome5():
    return 'Iam from welcome5'
# welcome5()

print(welcome5())

# anonymous functions or also called lambda function
# syntax of lambda functions
# function name=lambda arguments:expression


# def double(x):
#     return x*2
# result= double(10)
# print(result)
# print(double(30))  

duigun= lambda x:x*2
print(duigun(50))

# function with return value
def add (x,y):
    return x+y

def sub (x,y):
    return x-y     

def mul (x,y):
    return x*y

def div (x,y):
    return x/y     

print(add(2,5))    
print(sub(2,5))    
print(mul(2,5))    
print(div(10,10))    
   

# using arbitrary key word arguments

def build_profile(first,last,**kwargs):
    profile={}
    profile['First_Name']=first
    profile['Last_Name']=last
    for key,value in kwargs.items() :
        profile[key]=value
    return profile 

print(build_profile('Hasibur','Arman',location='Dhaka',field='IT'))

import math
print(math.pi)










    

    
