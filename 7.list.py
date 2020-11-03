'''
All Collection Types: (Array)

1. list (changeable, dublicate) []
2. tuple (non-changable, dublicate) ()
3. dictionary (changable, non-dublicate) {}
4. set (non-index form, non-dublicate) {}
'''

# create list: 
mylist = [1,'Hello',3,[4,2,1,3],5,(1,2,3,6)]
print('\nType: ', type(mylist), '\nLen: ', len(mylist), '\nMylist: ', mylist)

# List single index postion
print('\nMylist: ', mylist[3])

# Double index postion
print('\nMylist: ', mylist[3][2])

# Get last value from list
print('\nTuple: ', mylist[-1])

# Last index postion
print('\nTuple: ', mylist[-1][3])

# slice + postive and negative slicing
mylist = [2,3,4,5,6,7]
print('\nSLicing: ', mylist[1:4])

# create once class list
class_8 = ['Ram','Shyam','Seeta','Geeta']

# add new student in class
class_8.append('Vani')

# replace student by insert():
class_8[0] = 'Shree Ram'
class_8.insert(1, 'Poorva')

# to get index postion use index()
print('\nTo get Vani\'s Rollnumber: ', class_8.index('Vani'))

# Sort the list
class_8.sort()

# Reverse
# class_8.reverse()

# class_8 copy:
class_9 = class_8.copy()

# new admission in class 9
new_students = ['Raju','Reema','Seema']

# add class 9 and new stuents list
class_9.extend(new_students)

# Pop:
# class_9.pop()
class_9.pop(-2)

# remove()
class_9.remove('Raju')

class_9.clear()

print('\nClass 8th students: ', class_8)
print('\nClass 9th students: ', class_9)


'''
Question:

1. slice + postive and negative slicing in list
2. Check count method how it works?

Programming Questions:

1. Ek python file me multiline comment me list, tuple, set aur dict ke difference serch karke likhna hai.

2. List me positive and negative position values ko print kar ke check karna hai.

3. List me positive and negative slicing bhi print kar ke check karna hai.

4. Find the length of list?

5. Ek list bana hai jisme ki input ka use karke apne friends ke name insert karne hain.

6. Jo friend list banai hai usme se app kisi bhi friend ka name remove karna cahte ho aur aysa karne ke liye app input method ka use karke ye kaam karoge.
'''