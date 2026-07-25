data = {
    101: {'name': 'Ali', 'balance': 1000},
    102: {'name': 'Sara', 'balance': 500},
    103: {'name': 'Zohreh', 'balance': 2100},
    104: {'name': 'Babak', 'balance': 600},
    105: {'name': 'Hamid', 'balance': 750},
}

id = 101

item = data[id]

# print(item)

#Method 1

print(item['name'],'has',item['balance'],'units in their account')


#Method 2

s = item['name'] + ' has ' + str(item['balance']) + ' units in their account'
#join
m = (item['name'],'has',str(item['balance']),'units in their account') #Like A tupple

t = ' '.join(m)
print(s)
print(t)