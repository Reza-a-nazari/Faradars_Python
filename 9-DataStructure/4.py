from collections import namedtuple

Point = namedtuple('Point' ,('x' , 'y'))

def Add_point(p1:Point , p2:Point):
    p_Final = Point(p1.x + p2.x,p1.y + p2.y)

    return p_Final
p1 = Point(1,2)
p2 = Point(3,4)
print(Add_point(p1,p2))


#############
Point.__add__ = lambda self , p : Point(self.x + p.x , self.y + p.y)

print(p1+p2)

############

class ThePoint(Point):
    def __add__(self, p):
        return ThePoint(self.x + p.x , self.y + p.y)
a = ThePoint(1,2)
b = ThePoint(5,6)
print('ThePoint Class with ,ThePoint.__add__(a,b)\n : ',ThePoint.__add__(a,b))
print('ThePoint Class with a+b \n : ',a+b)