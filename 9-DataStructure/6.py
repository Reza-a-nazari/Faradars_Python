from random import randint
from collections import Counter
#===================================

A = [randint(1,10) for _ in range(10)]

c = Counter(A)

# print(c.most_common())
# print(c.elements)


c2 = Counter(cat =5 , mouse=2 , dog =4)
# print(c2)

c3 = Counter(cat =5 , mouse=2 , horse =4)
import copy
print(copy.deepcopy(c2 - c3))

