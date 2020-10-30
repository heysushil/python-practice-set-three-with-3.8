'''
Boolean Values:

1. Boolean values alwarys return Ture or False
2. Boolean values 0 ko False aur 1 to True as accept karta hai
3. Boolean method is bool()

Boolean Values kab False return karta hai:

1. bool(False)
2. bool(None)
3. bool(0)
4. bool('')
5. bool([])
6. bool(())
7. bool({})

Note: String me concatenae  or 1 se jada stirng ko marge karne ke liye hum + sign ka use karte hain.
C, C++ languages me concatenation ke liye .(dot) sign ka use kiya jata hain.
'''

print('\nFalse case: bool(False) :  ', bool(False))
print('\nFalse case: bool(None) :  ', bool(None))
print('\nFalse case: bool(0) :  ', bool(0))
print('\nFalse case: bool('') :  ', bool(''))
print('\nFalse case: bool([]) :  ', bool([]))
print('\nFalse case: bool(()) :  ', bool(()))
print('\nFalse case: bool({}) :  ', bool({}))


# condtion
name = input('\nEnter your name: ')

if bool(name) == True:
    print('\nHi ', name)
else:
    print('\nEmpty')

5 > 33
print('\n', )