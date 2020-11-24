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

print('\nParty details:\n')
for p in partylist:
    print('Hi, ' + p + ' , Welcome to party.')
