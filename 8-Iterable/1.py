# In [1]: A = [1,2,3,4]

# In [2]: square = lambda x: x**2

# In [3]: square(5)
# Out[3]: 25


######

#1
A = [1,2,3,4]

square = lambda x : x**2

# print(list(map(square,A)))


#2

square2 = lambda x : (x,x**2)

# print(list(map(square2,A)))


#3

# 
B = [5,6,7,8]
print(list(map(lambda x,y : x+y , A , B)))