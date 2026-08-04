A = list(range(20))
print(list(zip(*[iter(A)]*2)))

# In [15]: B = iter([1,2,3,4,5,6,7,8,9,10])

# In [16]: list(zip(B,B,B))
# Out[16]: [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

# In [17]:

#ُstrict = True !!!