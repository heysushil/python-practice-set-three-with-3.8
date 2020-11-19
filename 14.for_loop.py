'''
For loop ka work behavior:

1. For loop ka use kisi bhi sequacne ko print karne ke liye use hota hai.
2. Jaise ki hamare pas list, tuple, set and dictionary hai joki values ko sequence me dete hain.
3. Jaise ham ek example lete hain aur use print karke check karte hain.

For loop ka syntax:

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
'''

# for loop
numbers = ['Poorva',2,3,4,'Python',6,7.999,[8,9],10]

for vaani in numbers:
    # print(vaani, end="")
    print(vaani)

for i in range(3, 31, 3):
    print(i)

print('\nLen of numbers: ', len(numbers))

# use break in for loop
for data in numbers:
    # print(vaani, end="")

    # stop when find Python in list
    # if 'Python' in numbers:
    if 'Python' == data:
        # print('\nPython founded.')
        # break
        continue

    print(data)

mylist = ['Poorva',2,3,4,'Python',6,7.999,[8,9],10]
print('\nmylist len: ', len(mylist))

for m in mylist:
    if 'Poorva' == m or 'Python' == m:
        print('Hi ', m)
        continue

    # if 'Python' == m:
    #     print('Hi, ', m)
    #     break


'''
Question:

1. How to show for loop values on horizontal form
2. List ki specific postions ki values ko print karna hai for loop ke help se.
    Example: ['Poorva',2,3,4,'Python',6,7.999,[8,9],10]
        from python to [8,9]


Other Programs:

Note: Sare program for loop ka use kar ke banae hain.

1. 1 to 100 number print karna hai.

2. user se input lena hai koi bhi single number and uska table (Pahada) print karan hai. Aur iska range 10 tak rahega.

3. User se 2 input lena hai ek staring point aur 2nd end point ke liye aur usko print karna hai.
    
    Important Point:

        1. Agar user first input greater then second number de raha hai then usko message show karna hai ki ye possible nahi hai.
        2. Agar user input me number ki jagha alphabets deta hai to bhi user ko message show karna hai ki ye posible nahi hai pleas enter only number.
        3. Finally agar user inputs sahi deta hai then user ko wo complete range ka numebrs show karane hai.

Note: Question number 4 ke liye reserch ki jarurat padegi.

4. List me last index number kya hai ye pata karna hai? List me last value kya hai ye nahi pata karna hai. But...
    Example:
        Is list me [1,2,3,4,5,6,7,8]
        Last index postion 7 hai.
    Case:
        a. Ye case sabse pahle ek number list me without dublicate valeus ke last index position find karna hai.
        
        b. But agar list me multiple dublicate values hain then is list ka use karke ye pata karna hai ki last 7 ka index number kya hai:
        [1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7]

5. 2 list hain jinke data ko side by side show karan hai:
    Example lists:
        fields = ['name','mobile','address']
        names = ['ram',9989879879,'India']

    For loop ka use karke inko side by side show karna hai?

6. Jaise for loop me else ka use kiya gaya hai wise hi while loop me user se 2 numebrs ka input lena hai aur in case agar starting number 1 se greater hai to number not accetp ka message show karan hai.

Otherwise agar end number greater then 10 hai to not accept ka mesage show karan hai.

Otherwise numbers ko print karna hai and at last while loop end ke bad else ka use karke while loop stoped ka message show karna hai.
'''