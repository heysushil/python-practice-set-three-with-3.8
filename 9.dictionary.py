'''
Dictionary in Python:

About Assosiative Array:

1. C, C++ ya php me hame assosiative array milta hai.
2. Synatx: variableName = array('name' => 'Sushil')
3. Assosiatve sysntax me array(key => value)
4. Yahi same concept of associative array python me Dictionary ke name se use hota hai.

Python me dictionary ko use karne ke liye:

1. Syntax: newvalue = {'key or userDefinedName' : 'value or userDefinedValue',}
2. Tupel me () small bracke ke agar koi single value define ki jaye to wo tuple type nahi hai because tuple ke liye last me comma dena jaruri hai.
3. Waise hi dictionay me {} ke andar key:value ke bad comma dena jaruri hai. Other wise same braket ka use set me bhi hota hai. Aur dono confilt ho jata hai.
'''

# cerate new dictinary
# mydata = {'name' : 'Vaani', 'course' : 'Python'}
mydata = {
    'name' : 'Vaani',
    'course' : 'Python',
}
print('\nmydata type: ', type(mydata))
print('\nMydata: ', mydata['name'])

# multilevel dict:
bigdata = {
    'vaani' : {
        'course' : input('\nEnter your name: '),
        'mobile' : 9899898932,
    },
    'poorva' : {
        'name' : 'poorva',
        'course' : 'ai',
        'mobile' : 9899898932,
    },
    'seeta' : {
        'name' : 'poorva',
        'course' : 'ai',
        'mobile' : 9899898932,
    },
    'geeta' : {
        'name' : 'poorva',
        'course' : 'ai',
        'mobile' : 9899898932,
    },
    'meeta' : {
        'name' : 'poorva',
        'course' : 'ai',
        'mobile' : 9899898932,
    },
}

print('\nPoorva\'s coruse name:', bigdata['poorva']['course'])

print('\nHi my name is {} and I\'m learning {}.'.format(bigdata['poorva']['name'], bigdata['poorva']['course']))

# dict methods
# mynew = list(mytuple)
print('\nComplete Big data: \n', bigdata)

# use to remove last key value from dict
bigdata.popitem()

bigdata.pop('vaani')

print('\nBig data: \n', bigdata)

print('\nKeys: ', bigdata.keys())

print('\nValues: ', bigdata.values())

mykeys = ['name', 'mobile']
myvalues = ['vaani', 998797987]
print(bigdata.fromkeys(mykeys, myvalues))

print('\nsetdefault: ', bigdata.setdefault('hello'))
bigdata['hello'] = 'hi'
print('\n', bigdata.get('ram'), ' Final data: ', bigdata)

'''
Question:

1. what is array?
2. How many types of array?

Program:

1. Apne alag-alag friedns ka data set bana hai using dict and in sabhi friends ke detail ko dict mese multi line stirng ka use karke show karna hai.

Example: Output
----------------------------------------
        FriendName Data
----------------------------------------
Name: ____________
Email: ____________
Address: __________________
Mobile: ______________________

2. Jo upar friends dict banaya hai useme kuch new friends ko add karna hai and old friends ko remove karna hai alag se.

Aur ye kaam karne se pahle apne old friend list ka ek backup bhi lena hai.
'''