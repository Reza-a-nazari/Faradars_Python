data = {
    101: {'name': 'Ali', 'balance': 1000},
    102: {'name': 'Sara', 'balance': 500},
    103: {'name': 'Zohreh', 'balance': 2100},
    104: {'name': 'Babak', 'balance': 600},
    105: {'name': 'Hamid', 'balance': 750},
}

id = 101

item = data[id]

#Method 6

s = '{} has {} units in their account.'.format(item['name'],item['balance'])

print(s)

#Method 7

s = '{name} has {balance} units in their account.'.format(name =item['name'],balance =item['balance'])

print(s)


#Method 8

s = '{name} has {balance} units in their account.'.format(**item)

print(s)