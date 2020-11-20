# use multipal time or in single line
mylist = ['Poorva',2,3,4,'Python',6,7.999,[8,9],10]
for m in mylist:
    if 'Poorva' == m or 'Python' == m or 2 == m or m == 10:
        print('Hi ', m)
        continue

# pass list as argument in fucntion
def pass_list_on_function_as_argument(single_argument, second_list, myinfo):
    print('\nMy list\n', single_argument)
    print('\nMy second list\n', second_list)
    # print('\nMy thired list\n', myinfo)
    print('Hi, {}'.format(myinfo.get(1)))


myinfo = {
    'name':'Vaani',
    'course':'Python',
    0: 'Vaani',
    1: 'Poorva',
}

pass_list_on_function_as_argument(mylist, [1,2,3,4,5], myinfo)

# name = 'Vaani'

# print('\nHi, {}'.format(name))

# Ye funciton definition hai
# Yaha par fucntion ka jo ek work decide kiya gaya hai wo karna hai.
# like as: hame 2 humber ka sum karna hai to hum ko 2 arguments ki requirment hogi.
# jiske liye hum fucniton definine karte time 2 arguments hamare function ke ansar pass karenge.

def myfun(mylist):
    print('\nType: ', type(mylist), '\nLen: ', len(mylist), '\nMylist: ', mylist)
    
    info = '\nType: ', type(mylist), '\nLen: ', len(mylist), '\nMylist: ', mylist
    return info

mylist = [1,'Hello',3,[4,2,1,3],5,(1,2,3,6)]

result = myfun(mylist)
print(result)


# user define sum funciton
'''
Ye funciton 2 numbers ke sum ke liye hai.
Yaha par mere funcitonko 2 arguemtns num1 aur num2 ki requirments hai
ye numbers interger number honge ye mujhe dhyan rakhna hai.
'''
def mysum_function(num1, num2):
    '''
    Yaha par hame num1 aur num2 ki values mil chuki hain.
    Inko sum karne ke liye ek aur variable ki jarurat hai
    Iske liye main num3 variable banaungi.
    Then us variable ke andar num1 aur num2 ka sum karungi.
    '''
    num3 = num1 + num2

    '''
    Ab mujhe num3 vairbale ko print karna hai
    Taki main num3 ka answer dekh saku
    '''

    print('\nSum: ', num3)


'''
Ab yaha par jo funciton main define kiya hai usko call karungi.
Is funciton ko call karne se hi main iske andar ke work aur uska output dekh sakti hun.
Dhyan rahe agar funciton define karte time main funciton me argumets bhi diye hain. 
To function ko call karte time utne hi arguents pass karna jaruri hai.
'''
num1 = int(input())
mysum_function(num1, 1000)

