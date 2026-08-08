# [exp for item in container]
# [exp for item in container if condition]

# A = list(range(1,11))
# print(A)
# del A[0]
# print(A)

B = [x**2 for x in range(1,10)]

B2 = [x**2 for x in range(1,10) if x%2] #odd

print({x:x**2 for x in B})