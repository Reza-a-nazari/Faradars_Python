#SipHash
#Fowler-Noll-Vo

# print(hash('Hello world'))


#Exercise

class student:
    def __init__(self,id:int,name:str,age:int):
        self.id = id
        self.name= name
        self.age = age
    def __hash__(self):
        return hash((self.id , self.name , self.age))


person1 = student(403521521,'Reza',20)
person2 = student(403521521,'Reza',20)

phash1 = student.__hash__(person1)
phash2 = student.__hash__(person2)

if(phash1== phash2):
    print("Same Value")
else:
    print("Not same")



# In [14]: hash([1,1,3])
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# Cell In[14], line 1
# ----> 1 hash([1,1,3])

# TypeError: unhashable type: 'list'

# In [15]: hash(tuple([1,1,3]))
# Out[15]: 2966401914035743144