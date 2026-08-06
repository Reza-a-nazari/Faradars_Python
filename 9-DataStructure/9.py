from collections import ChainMap

family = dict(food='Pizza', drink='Dough', team='AC', city='London')

son = dict(food='Kebab', team='FC', os='Windows', proglang='Python')


ch = ChainMap(son,family)

print(ch.parents)