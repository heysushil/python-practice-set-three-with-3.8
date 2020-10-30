# multiline string


message = '''
Note: String me concatenae  or 1 se jada stirng ko marge karne ke liye hum + sign ka use karte hain.
C, C++ languages me concatenation ke liye .(dot) sign ka use kiya jata hain.
'''

name = 'Vani'

# use len() method to find length
print('\nName len: ', len(name))

# string char ko indiviual index postions par store karta hai

# get index
print('\nGet Name: ', name[0])

# find last char of stirng by -1
print('\nGet Name: ', message[-2])

# slicing [start:end]
print('\nStart: ', name[0:])

# jab end use karte hain then ye n-1
print('\nEnd: ', name[:3])


name = 'vani'

print('\nUpper: ', name.upper())


# String scape char:
print('\nVani\'s')
print('\tOne tab spcae')

print('\nname.capitalize(): ', name.capitalize())
print('\nname.upper(): ', name.upper(), ' Single Letter: ', name[1].upper())

name = 'Hello hi how are you hi again'
print('\n n a m e . c o u n t ( ) : ', name.count('hi'))

# name.index(): Ye indivial string char ki index postion find karne ke liye hai.

# name.isalpha(): True if string is only contain alphabets
# name.isalnum()
# name.isdecimal() vs name.isdigit()
# name.replace()

name = 'Diff. b/w name.isdecimal() vs name.isdigit() vs name.isnumeric()'
print(name.split(' '))


# string with format
name = input('\nEnter your name: ')
course = 'Python'
address = 'India'

# + concatanation sign use to join two strings togater

# print('\nHi, ' + name + ' I\'m learning ' + course)
print('''
--------------------------------
        {0}'s Details
--------------------------------
Name: {0}
Course: {1}
Address: {2}  
'''.format(name, course, address))






'''
Question:

1. Negative slicing.
2. Diff. b/w name.isdecimal() vs name.isdigit() vs name.isnumeric()

3. Create biodata using multiline string and format:

------------------------------------------
            name's Bio Data
------------------------------------------
My name is 
My class is
.
.
.
.
.
.
.            
'''