from collections import namedtuple

Location = namedtuple('Location' , 'x y name')

# print(dir(Location))

a = Location(10,20,'Tehran')
print(a)
b = Location(x=30 , y = 40 , name='Dallas')
print(b)


print(a.x)

print(a._replace(x=11))

print(a._asdict())