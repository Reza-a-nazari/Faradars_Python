s = 'ABCDEFGHIJ'


it = (iter(s))

# while(True):
#     try : 
#         print(next(it))
#     except :
#         break
## print(next(it))

# aaa =it.__length_hint__()

# print(aaa)



#####################
#####-----------#####
# Are They the Same?#   
#####################
#####-----------#####

###1

# T1 = list(iter(input , '.'))

# print(T1)


###2

T2 = []

while(input() != '.'):
    T2.append(input())

for i in T2 :
    print(i)


