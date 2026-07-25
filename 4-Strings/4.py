data = {
    101: {'name': 'Ali', 'balance': 1000},
    102: {'name': 'Sara', 'balance': 500},
    103: {'name': 'Zohreh', 'balance': 2100},
    104: {'name': 'Babak', 'balance': 600},
    105: {'name': 'Hamid', 'balance': 750},
}

id = 101

item = data[id]


#Method 9 (f-string)


name = item['name']

balance = item['balance']

s = f'{name} has {balance} units in their account.'

print(s)


#Method 10 (f-string with expression)


s = f'{item['name']} has {item['balance']} units in their account.'

print(s)
