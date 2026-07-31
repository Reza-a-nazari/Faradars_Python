A = [1,2,3,4,5,6,7]


# print(list(map(lambda x: x%2 ==0 , A)))

print(list(filter(lambda x : x%2 , A)) , 'odd') # odd

print(list(filter(lambda x :1 - x%2 , A)) , 'even') # Even


B = [1,0,1,1,1,0,1,4,0,5,6,7,8,0]

print(list(filter(None,B)) , "deleted 0s")