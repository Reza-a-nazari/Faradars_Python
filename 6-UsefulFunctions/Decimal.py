# print(0.1 + 0.2) # out 0.30000000000000004


from decimal import Decimal 
import math
# print((Decimal('0.1') + Decimal('0.2')))


# print(math.pi.__round__(2))

from decimal import getcontext

getcontext().prec = 4

# print(Decimal('0.1')/Decimal('0.3'))


from decimal import localcontext

with localcontext() as l : 
    l.prec = 100
    print(Decimal('1')/Decimal('56'))