#Method 4
data = {
    101: {'name': 'Ali', 'balance': 1000},
    102: {'name': 'Sara', 'balance': 500},
    103: {'name': 'Zohreh', 'balance': 2100},
    104: {'name': 'Babak', 'balance': 600},
    105: {'name': 'Hamid', 'balance': 750},
}

id = 101

item = data[id]
s= '%s has %s units in their account.' %(item['name'],item['balance'])
print(s)


#Method 5

# s= '%(name)s has %(balance)s units in their account.' %{'name':item['name'],'balance':item['balance']}
s= '%(name)s has %(balance)s units in their account.' %item
print(s)