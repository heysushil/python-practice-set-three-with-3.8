'''
Python me Loop ka use and work case.

Python me hame 2 loop case milte hain.

1. while loop
2. for loop

Note: Waise other programming languages like C, C++, PHP me hame 3 loop case milte hain. For, while, do-while. Also C, C++ jaise lanagauge me increment (++) aur decrement (--) use hota hai but python me ye use nahi hota hai.

Loop ka use kyo karte hain?

1. Loop same type ke repated work ke liye use hota hai.
2. Sequence datatype - list, tuple, range ye values ko index form me sotore rakhte hain. Inka use loop me values ko one by one print karne ke liye kiya ja sakta hai.
3. Ya fir kisi bhi collection of data like database table data ko bhi hum loop ke through print kara sakte hain.
4. Loop me pre aur post increment aur decrement hote hain.

While loop ka syntax:

intilization
while (condtion):
    body of while loop
    increment or decrement

While loop syntax ke baare me:

1. Intilization me koi bhi starting point decide karna hota hai. Like i = 1, Becasue loop ko hamesa starting and ending point ki need hoti hai.
2. while (i <= 10): Ye condtion hogi ki loop ko kaha tak chalna hai.
3. While body: yaha par jo kuch bhi print karna hai ya fir koi loop ya condtion chalana hai. Wo sab kuch yaha par kiya ja sakta hai.

For loop syntax:

for intilization in collectionOfValues:
    body of for loop

For loop syntax ke baare me:

1. For loop me intilization kewal variable ka hoga isme koi bhi value assign nahi karna hai. Becasue jo collection values hai usme se one by one values intilization ko recive hoga and wo usko for loop ke body ko pass karega.
2. Collection of values: Ye koi bhi collection ho sakta hai. Like as:
    a. list collection
    b. tuple collection
    c. range collection
    d. database tabel data collection
    e. so on....

If aur while loop me difference?

1. If Condtion agar sahi hai to wo condtion body me aayega aur wahi work stop ho jayega.
2. While loop me jab tak condtion sahi hai tab tak loop chalta ranega.
'''

# while loop

# print number 1 to 10
# first initialization of starting point

# setup 1
start = 3

# if start > 1:
#     print('\nyes')

# exit()

# setup 2: Check condtion if right then enter in while loop else terminate loop
while start <= 30: # ye tab tak chalega jab tak less then hai 10 se
    # setup 3: print your message
    print(start)

    # step 4: Increment or Decrement
    # increment start with 1
    start += 3 # start = start - 1

    # At last step 2 to step 4 repet till wrong conditon

'''
Program:

1. User se input lekar table print karna hai. Kewal starting ke 10 numbers print karne hain. Jisme ki user se 2 input lena hai:
    1. table start number
    2. table end number

2. 1st program me same work karna hai but user se single input lekar karna hai.

3. Same 1 program decrement order me karna hai.

4. Same 2nd program decerment order me karna hai.
'''

# --------------- 1st program -----------------------
'''
1. User se input lekar table print karna hai. Kewal starting ke 10 numbers print karne hain. Jisme ki user se 2 input lena hai:
    1. table start number
    2. table end number
'''

start = int(input('\nEnter starting number: '))
end = int(input('\nEnter end number: '))


while start <= 50:
    print(start)
    start += 1


print('\nstart: ', start + 1)

'''
Problem:

1. Program 1 solution me problem ki user agar start value 10 and end value 1 input karta hain then loop me problem aaygi isko kaise handel karen.
'''
