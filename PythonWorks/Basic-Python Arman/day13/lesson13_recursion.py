'''
Python Recursipon
-------------------
A function that calls itself.
Recursion is the process of defining something in trems of itselfs.

HW===> fibonnacci element using recursing method

'''

# Factorial using loop
# 3! = 3x2x1

fact=1
num= int(input('Enter a value for factorial: '))
for i in range(1,num+1):
    fact= fact*i

print(f'The factorial of {num} is {fact} ' )



# Factorial using recursive method

def factorial (n):
    if n==0:
        return 1
    else :
        return n*factorial(n-1)
            
'''
factorial(4)
    4*factorial(4-1)
    4*3*factorial(3-1)
    4*3*2*factorial(2-1)
    4*3*2*1*factorial(1-1)
    4*3*2*1

'''    
print(f'The factorial of {num} is {factorial(num)} ' )
print(factorial(7))




