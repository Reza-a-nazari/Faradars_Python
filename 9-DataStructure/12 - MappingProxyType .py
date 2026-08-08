from types import MappingProxyType

data = {'Ali' : 1 , 'hossein' : 2 , 'Reza' : 3}

mpt = MappingProxyType(data)

#It Won't change
# mpt['Ali'] = 4

print(mpt)

#It Will be changed

data['Ali'] = 4

print(mpt)