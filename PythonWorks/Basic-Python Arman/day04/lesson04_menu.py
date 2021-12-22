'''

'''

while True:
    print('Main Menu')
    print('1. Addition')
    print('2. Substraction')
    print('3. Multiplication')
    print('4. Divition')
    print('5. Modulus')
    print('6. Exponent')
    print('7. Exit')

    print('Enter your selection:', end='')

    choice= int (input())
    if choice == 1:
        a= int (input('Enter value for a: '))   
        b= int (input('Enter value for b: '))   
        print('Addition is %s '%(a+b))
    elif choice== 2 :
        a= int (input('Enter value for a: '))   
        b= int (input('Enter value for b: '))   
        print('Substraction is %s '%(a-b))

    elif choice== 3 :
        a= int (input('Enter value for a: '))   
        b= int (input('Enter value for b: '))   
        print('Multiplication is %s '%(a*b))

    elif choice== 4 :
        a= int (input('Enter value for a: '))   
        b= int (input('Enter value for b: '))   
        print('Divition is %s '%(a/b))


    elif choice== 5 :
        a= int (input('Enter value for a: '))   
        b= int (input('Enter value for b: '))   
        print('Modulus is %s '%(a%b))

    elif choice== 6 :
        a= int (input('Enter value for a: '))   
        b= int (input('Enter value for b: '))   
        print('Exponent is %s '%(a**b))

    elif choice==7:   
        print('Thank you')
        break
    else:
        print('Sorry invalid selection')