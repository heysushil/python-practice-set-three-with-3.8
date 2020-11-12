# Shoping example:

myshoping_list = ['a','b','c']

shope = ['a','s','d','c','b']

item = input('\nEnter your itam name: ')

if item in shope:
    print('\nYes, it\'s price is ')


# Create list of students
myclass = ['Ravi','Kishan','Harry','Garry']

# print('\n==: ', 5 == 5); print('\nis: ', 5 is 5, ' address: ');

# get student name by input
name = input('\nEnter your name: ')

# if name == myclass[0]:
#     print('\nkoi bhi message')

# name = 10; name1 = 10
# print('\nName add: ', id(name), ' Myclass add: ', id(name1))

if bool(name) == False:
    print('\nHi, ',name)
    # nested condtion to chek is studetn availablae in myclass or not
    if name in myclass:
        print('\n' + name + ' present.')
    else:
        print('\nNot present.')
else:
    print('\nEmpty values not allowed.')


exit()

# Example:

print('\n\nExample: ')
a = int(input('\nEnter A value: '))
b = int(input('\nEnter B value: '))
# c = input('\nEnter C value: ')

# print('\nA len: ', len(a))

if a > b:
    print('\nHello A')
else:
    print('\nHello B')


