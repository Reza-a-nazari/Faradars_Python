class A :
    name = 'name'
    __var = 'A'

    def __init__(self,name,var):
        self.name = name
        self.__var = var
class B(A):
    def __init__(self,name,var):
        self.name = name
        self.__var = var

#Name Mangling usage in Python -> __var

a = A("First A" , 1000)
b = B("First B" , 500)
print(a)
print(b)