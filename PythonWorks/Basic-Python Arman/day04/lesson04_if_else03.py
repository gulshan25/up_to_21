"""
example of nested if

"""
Username=input('Enter user name:')
password=input('Enter password :')

if Username.upper()=='Admin'.upper() and password=='arman':
        print(f'Welcome Mr. {Username}')
elif Username.upper() != 'Admin'.upper() and password == 'arman':
    print('invalid user name')
elif Username.upper() == 'Admin'.upper() and password != 'arman':
    print('invalid password')

else:
    print('Username and Password both are wrong')

        
