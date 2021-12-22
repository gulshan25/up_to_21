'''
File Handling
---------------
To open a file object in python is 
file_object=open('file_name','mode')
The modes are:
'r'===> read mode
'w'===> write mode
'a'===> append mode


'''
f=open('arman.txt','w')
f.write('This is our new text file\n')
f.write('This is another line\n')
f.write('Arina  and ss bhai ajke kothay gelo??\n')
f.close()


# Open a file for read mode
file=open('arman.txt','r')
print(file.read())
#print(file.read(7))
#print(file.readlines())


file.close()

# add some more data

f=open('arman.txt','a')
f.write('It is a new file\n')
f.write('it is a different file\n')
f.write('sujon raajbongshi ar late krbe na\n')
f.close()

file=open('arman.txt','r')
print(file.read())
