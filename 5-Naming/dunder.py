#Name mangling


class A :
    name = 'A'
    _type = 'Unknown'
    __var = 'AB'


print(A.name)
print(A._type)
# print(A.__var) ERROR
# print(dir(A))
print(A._A__var)

