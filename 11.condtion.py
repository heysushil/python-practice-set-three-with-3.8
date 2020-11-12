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


'''
Programmes for practice:

1. User se 2 input lo and check karo ki agar 1st input bada hai to useke liye message show karo otherwise second ke liye message show karo.

2. Ek shoping list banao, aur iske bad me check karo ki shoping list me who iteam hai ya nahi hai jo tum shop par jane ke bad shopkeeper se puch rahe ho. Iske liye product varaible create karna and then check karna hai.

Agar item list me hai then shopkeeper se uska price pucho?
Then agar price acceptable hain means yes or not wala case?
Then item no purchase karo and show item bill, jisme ki-
    1. Item purchase date
    2. Item order number
    3. Item Price
    4. Iteam name
Included ho. Is ouput ko representative way me show karna hai.

3. user se name recive karna hai aur check karna hai ki agar user name me koi value deta hai to name print ho otherwise: plesa enter your name ka message show ho.

4. Program bana hai ki jisme 3 alag-alag number user se lene hai aur ye following condtion bana hai:
    a. agar first value greater hai then first user win
    b. agar second value greater then second user win
    c. same for thired user
    d. agar sabhi ke number same hai then tie ka message
    e. agar koi number galt enter hua to uska message
    f. sath me winer user ke liye ek alag se grand message aap ke tarike se jo bhi best output show kara sako.

    a, b, c:


5. Ek friend list bana hai aur agar uske sath me condtion lagana hai ki:
    a. User kisi bhi random friend ko check karna chata hai ki kya wo party me hai ya nahi. Uski madad karo ye check karne me. 

    b. Agar friend party me nahi hai then User usko party me add karna cahta hai. Uski madad karo uske friend ko party me add karne ke liye.

    c. User, jis friend ko serach kar raha hai agar wo present hai to user ko uske bare me batao.

    e. User ek friend ko party se nikalna chata hai uski madad karo. Aur jab wo friend se nikal jaye to user ko batao ki wo friend party se gaya.

Note: In question ke liye aap ko apne hisab se soch kar program karna hai aur ye sare question ke liye abhi tak jo padha hai unhi ka use karna hai.
'''
