import copy


a = [1,2,3,4]
#not work with b = a if change a 
b = copy.copy(a) #Shallow Copy


A = [[1,2],[3,4,5],[6,7,8,9,10]]

B = copy.deepcopy(A) #DeepCopy

print(B)