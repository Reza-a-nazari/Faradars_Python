A = [1,2,3,4,-6,7,8,9,10]

# print(max(A))
# print(max(A,key=lambda x:x**2))
# print(max(A,key=lambda x:-x))



data = [
{'Name': 'A', 'Age': 10, 'Revenue': 100},
{'Name': 'B', 'Age': 8, 'Revenue': 90},
{'Name': 'c', 'Age': 15, 'Revenue': 120},
{'Name': 'D', 'Age': 5, 'Revenue': 60},
]

#find the oldest
# oldest = sorted(data,key=lambda x:x['Age'],reverse=True)
oldest = max(data,key=lambda x:x['Age'])
print(f'{oldest=}')

#find the richest 
richest = max(data,key=lambda x:x['Revenue'])
print(f'{richest =}')

#find the most efficient 
efficient = max(data,key=lambda item:item['Revenue']/item['Age'])
print(f'{efficient=}')


#With def

def get_age(item):
    return item['Age']


print(max(data,key=get_age))