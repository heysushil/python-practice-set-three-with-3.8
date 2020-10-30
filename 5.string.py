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


print('\nUpper: ', name.upper())


'''
Question:

1. Negative slicing.
'''