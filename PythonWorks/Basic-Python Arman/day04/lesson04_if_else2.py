"""
example of combination of condition

"""
Username=input('Enter user name:')
password=input('Enter password :')
if Username.upper()=='Admin'.upper() and   password=='arman':
        print(f'Welcome Mr. {Username}')
   
    
else:
    print('invalid user')

        