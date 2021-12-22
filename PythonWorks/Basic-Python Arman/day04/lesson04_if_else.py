"""
example of nested if

"""
Username=input('Enter user name:')
password=input('Enter password :')
if Username.upper()=='Admin'.upper():
    if password=='arman':
        print(f'Welcome Mr. {Username}')
    else:
        print('Invalid password')
else:
    print('invalid user')

        
