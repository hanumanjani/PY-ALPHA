d1 = {}
otherdict = {1:'hanuman'}
d = {'key': 'value'}
d = {k: v for k, v in [('key', 'value')]}

# makes a shallow copy of otherdict
d1 = {**otherdict}
print(d1)
# also updates the shallow copy with the contents of the yetanotherdict.
d2 = {2:'ram'}

d3 = {**otherdict, **d2}
print(d3)

# BUILT IIN CLASS
d = dict() #empty dict
print(d)
d = dict(key='value')
print(d)
d['newkey'] = 47
print(d)
d['newlist'] = [1, 2, 3]
print(d)
d['nested_dict'] = {1:'hr'}
print(d)
del d['newkey']
print(d)

d_d3 = {**d, **d3}
print(d_d3)
# CHAIN
from itertools import chain
print(dict(chain(d.items(), d3.items())))
# CHAINMAP
from collections import ChainMap
print(dict(ChainMap(d, d3)))
print(d.keys())
print(d.values())
print(d.items())
# print(d.__doc__)
print(d['nested_dict'])
d['newlist'].append(4)

print(d)

# We can also create a dictionary using a list of two-items tuples
iterable = [('eggs', 5), ('milk', 2)]
dictionary = dict(iterable)
print(dictionary)
# Or using keyword argument:
dictionary = dict(eggs=5, milk=2)
print(dictionary)

# Another way will be to use the dict.fromkeys:
dictionary = dict.fromkeys(('milk', 'eggs'))  # => {'milk': None, 'eggs': None}
print(dictionary)
dictionary = dict.fromkeys(('milk', 'eggs'), (2, 5)) # => {'milk': 2, 'eggs': 5
print(dictionary)


print(dict(a=1, b=2, c=3))# {'a': 1, 'b': 2, 'c': 3}
print(dict([('d', 4), ('e', 5), ('f', 6)]))# {'d': 4, 'e': 5, 'f': 6}
print(dict([('a', 1)], b=2, c=3))# {'a': 1, 'b': 2, 'c': 3}
print(dict({'a' : 1, 'b' : 2}, c=3)) # {'a': 1, 'b': 2, 'c': 3
