A = [1,2,3,4]

B = {1,2,3,4}


def print_1():
    for i in range(0,len(A)) :
        print(A[i] , end=" ")

def print_2():
    for i in range(0,len(B)) : # Impossible
        print(B[i], end=" ")

# print_1()
print_2()