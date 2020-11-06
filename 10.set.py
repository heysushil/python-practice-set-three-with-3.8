'''
Set in python:

Important points to set:

1. Set ko {} is braket se denote karete hain.
2. Set values ka koi order nahi hota hai. Means values ko agar index position ke behalf par feach karna caho to error milega.
3. Set me values hamesa unique honge.
4. Set values hamesa suffle karte rahete hain.

Set ka use collection of set me se dublicacy remove karne ke liye kiya jata hai.

Set ka use ek se jada set ko apas me mager karn ke liye aur sath me dublicate valeus ko filter karne ke liye kiya jata hai.
'''

programming = {'Python','C++','C','PHP','Java','JavaScript'}
development = {'mobile','web development','GUI','scripting'}

# print('\nmyset type: ', type(myset), ' Check empty? ', bool(myset))
print('\nProgramming len: ', len(programming) + len(development))

programming.add('Pascal')
otherprogramming = ['html','css','jquery']
programming.update(otherprogramming)

# programming[0]

print('\nProgramming: ', programming)

# programming.

'''
Use these methods to complete task:

1. use union(): to join two sets
2. use intersection()
3. issubset()
4. issuperset()
'''


'''
Question:

1. How many words in Oxford dictionary?
2. diff b/w pop and remove?
3. why pop method is not good for set?
4. diff b/w remove and discard method?
5. diff b/w union and update method?
'''