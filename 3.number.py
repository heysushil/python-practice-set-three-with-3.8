'''
2. Numeric Types: Ye sabhi number accept karene wale datatype hain
    a. int: integer = Ye positive aur negative dono hi number accept karta hain. Example: a = 10 | a = -10
    b. float: float = Iska use point number ke liye hota hai. Example: a = 10.10 | a = -10.10
    c. complex: complex = j . Isme hame kisi bhi int ya float value ke sath small j use hua ho to wo complex number hai. Example: a = 10j | a = -10.10j
'''

'''
About input and print:

print(): for output 
input(): for input
'''

# int
int_number = -100

print('\nint_number: ', type(int_number))


float_number = -100.00

print('\nfloat_number: ', type(float_number))


complex_number = int_number + 200j
print('\ncomple_number: ', type(complex_number), ' Value: ', complex_number)


# type converstion

print('\nInt to float con: ', float(int_number), 'Type: ', type(float(int_number)))

print('\nFloat to int: ', int(float_number), ' Type: ', type(int(float_number)))

mynewcomplex = complex(int_number)
print('\nInt to complex: ', complex(int_number), ' Type: ', type(complex(int_number)))


# print('\nComplex to int: ', int(complex_number))

name = '10'
print('\nName: ', name, ' Type: ', type(name))

message = '\nStr to int: '
str2int = int(name)
newtype = ' Type: '
checkType = type(int(name))

print(message, str2int, newtype, checkType)

name = int(input('\nEnter your name: '))
print('\nName type: ', type(name), ' Value: ', name)


'''
number system: 

1. binary 2 (0b) (0,1)
2. octal 8 (0o) (0-7)
3. decimal 10 (0d) (0-9)
4. hexadecimal 16 (0x) (0-F) (10-A, 15-F)

Note: 

1. octal pair: 111 | 421
2. decimal pair: 1111
'''
print('\nBinary to octal: ', 0b010)
print('\nHexa to octal: ', 0xF)
print('\nOctal: ', 0o07)


'''
Questions:

1. What is low level and hight level languages?

2. How to print decimal number
'''