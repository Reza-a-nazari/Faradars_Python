A = [1,2,3,4]

B = [10,20,30,40]

#1

# for i in range(len(A)):
#     print(A[i],B[i])

#2

# C = list(zip(A,B))
# print(C)


#3 

C = "Byee"
L = list(zip(A,B,C))

print(L)


Zip2 = list(zip(L[0],L[1],L[2],L[3]))
print(Zip2)
print(list(zip(*L)))