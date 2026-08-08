from typing import NamedTuple

class Point(NamedTuple):
    x : int
    y : int

a=  Point(10,20)
print(a)

# pip install ypstruct

from ypstruct import structure

empty_points = structure(x=None , y=None)

points = empty_points.repeat(10)


print(points)