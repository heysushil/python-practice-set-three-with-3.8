programming = {'Python','C++','C','PHP','Java','JavaScript'}
print('\nprogramming: ', programming)

# print('\nCheck python is in set or not: ', 'Python' in programming)
name = input('\nEnter programming name from programming set: ')

if name in programming:
    programming.remove(name)
    print('\n' + name + ' is removed.')
    print('\nFinal programming set: ', programming)
