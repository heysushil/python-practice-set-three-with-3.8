def party_members_data():
    # creating a blank party list
    partylist = []

    party_limit = int(input('\nEnter party limit: '))
    # party_limit = 3
    if party_limit == 5:
        partylist = ['Poorva','Vaani','Ram']
        print('\n', partylist)

    # append multipal values on loop
    for i in range(party_limit):

        partylist.append(input('Enter name {}: '.format(i+1)))

    return partylist

# print all paarty memebrs name list
def members_list():
    partylist = party_members_data()
    print('\nParty details:\n')
    for p in partylist:
        print('Hi, ' + p + ' , Welcome to party.')
    
    options()

# call party members funciton
# party_members_data()
# members_list()

def options():
    option = int(input('\n1. Creater new party list\n2. Exit\n\nEnter your options: '))

    if option == 1:
        members_list()
    elif option == 2:
        print('\nYou are successfully exit form program.')
    else:
        print('\nWrong choice.')

# create opetion for users
option = int(input('\n1. Creater new party list\n2. Exit\n\nEnter your options: '))

if option == 1:
    members_list()
elif option == 2:
    print('\nYou are successfully exit form program.')
else:
    print('\nWrong choice.')
    options()
