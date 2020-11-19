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