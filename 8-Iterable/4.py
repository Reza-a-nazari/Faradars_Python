A = [1,-2,3,4,5,6,-7,8,9,10,-11]
# max_ = A[0]
# for i in range(len(A)):
#     if max_ < A[i] : 
#         max_ = A[i]
# print(max_)

#MySort

# for i in range(len(A)):
#     for j in range (i+1,len(A)):
#         if(A[j]>A[i]):
#             tmp =A[j]
#             A[j] = A[i]
#             A[i] = tmp
#         else : 
#             continue

# print(A)

#Selection Sort

# for i in range(len(A)):
#     max_index = i

#     for j in range(i+1, len(A)):
#         if A[j] > A[max_index]:
#             max_index = j

#     A[i], A[max_index] = A[max_index], A[i]
# print(A)


B = sorted(A,key=lambda x : x%2 )
A =sorted(A,reverse=True)


print(A,'A')
print(B,'B')


