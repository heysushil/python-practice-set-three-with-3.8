'''
Condition statments and practicale

Sytanx:

1. Jab single condition hoto:
    if your_condtion:
        your message. ye string ho ya kuch bhi ho sakta hai.

2. Jab single condition ho and ek default condtion ho to:
    if(your_condtion):
        your message. ye string ho ya kuch bhi ho sakta hai.
    else:
        your default message will be here.

3. Jab 1 se jada condition ho to:
    if(your_condtion):
        your message. ye string ho ya kuch bhi ho sakta hai.
    elif(your_another_condition):
        your message.
    else:
        default condition message.

4. Nested condition:
    if (your_condtion):
        Yaha par message dena chao to do ya nahi.

        if(condtion):
            your message.
        else:
            your message.
    else:
        default condition message.

Comparision conditional operations:

Note: Yaha par a aur b variable le kar example show kiya hai.

1. Equals: a == b
2. Not equals to: a != b
3. Less then: a < b
4. Less then or equal to: a <= b
5. Greater then: a > b
6. Greater then or equal to: a >= b
'''

a = 10
b = 20

# Singel condtion
if a > b: # This is condtions option body
    print('\nA is greater then b.')
    # this is condtions closing body

# if and else condtion
if a > b: # This is condtions option body
    print('\nA is greater then b.')
    # this is condtions closing body
else: # else is also known as default condtion
    print('\nB is greater then A.')

a = 10
b = 10
# Multipal condtions
if a > b: # This is condtions option body
    print('\nA is greater then b.')
    # this is condtions closing body
elif b != a:
    print('\nb >= a')
elif a == b:
    print('\nA is equal to b.')
elif b > a:
    print('\nB is greater then A.')
else:
    print('\nNon of them are right.')


# Logical operatores
a, b, c, d = 10, 20, 30, 40

# and or not
# if b > a and d > a and a != b:
if (b < a and d > a) or (a > b and a < b):
    print('\n3 condtions with and right')
elif c >= b and not(a > b and b > c):
    print('\nelif condition.')
else:
    print('\nNon of them right')

# in
mydata = ['Ram','Shyam']

if 'Ram' in mydata:
    print('\nJai Shree ', mydata[0])

name = input('\nEnter your name: ')

# print('\nBool: ', bool(name))

if bool(name) == True:
    print('\nHi, ' + name)
else:
    print('\nPleas enter your name.')


'''
PHP if condtion:

if(a > b){
print('Hello)
            print('Hello)
        print('Hello)
}
'''

# programming = {'Python','C++','C','PHP','Java','JavaScript'}
# print('\nprogramming: ', programming)

# # print('\nCheck python is in set or not: ', 'Python' in programming)
# name = input('\nEnter programming name from programming set: ')

# if name in programming:
#     programming.remove(name)
#     print('\n' + name + ' is removed.')
#     print('\nFinal programming set: ', programming)
