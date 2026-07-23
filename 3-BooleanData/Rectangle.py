class SpaceOfRectangle:
    def __init__(self,a,b):
        self.a = a 
        self.b = b
    def area(self):
        return self.a * self.b 

#Work WIth Pytest


class CheckSpace:
    def __init__(self,area):
        self.area = area
    def Check(self):
        if(self.area.area()==0):
            return False
        else:
            return True


Test1 = SpaceOfRectangle(10,1)
print(CheckSpace(Test1).Check(),"Excpect True")
Test2 = SpaceOfRectangle(10,0)
print(CheckSpace(Test2).Check(),"Excpect False")

    
