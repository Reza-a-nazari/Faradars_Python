#ipython
# In [4]: (x**2 for x in range(1,10))
# Out[4]: <generator object <genexpr> at 0x000001C6A8D39850>

# can go forward with next()

#use

max(x**2 for x in range(1,10))

#instead

max([x**2 for x in range(1,10)])