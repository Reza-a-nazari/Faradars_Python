
data = {
    101: {'name': 'Ali', 'balance': 1000},
    102: {'name': 'Sara', 'balance': 500},
    103: {'name': 'Zohreh', 'balance': 2100},
    104: {'name': 'Babak', 'balance': 600},
    105: {'name': 'Hamid', 'balance': 750},
}

id = 101

item = data[id]
#Method 11
from string import Template
Template = Template('$name has $balance units in their account')

s= Template.substitute(name = item['name'],balance = item['balance'])
# s= Template.substitute(**item)
print(s)