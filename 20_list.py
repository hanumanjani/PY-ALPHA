# LIST
a = [1, 2, 3, 4, 5]
a.append(6)
print(a)
b = [8, 9]
str1 = 'hello world'
a.append(str1)
print(a)
a.extend(b)
print(a)
a.extend(range(3))
print(a)
print(a.index(0))
a.insert(0, 0)
a.pop(0)
a.remove(2)
print(a)
print(a.count(1))
# a.sort()
print(a)
b.clear()
print(b)
b = ["blah"]*6
print(b)
a = list(range(10))
print(a[0:7:2])
del a[::2]
del a[-1]
print(a)
b = list(a)
print(b)
"""
zip return a list of touple

"""
alist = ['a1','b1','c1']
blist = [1,2,3]
for a, b in zip(alist,blist):
    print(a,b)

# LIST COMPREHENSIONS------------------------------------------->
# [ <expression> for <element> in <iterable> ]
# [ < expression >for < element > in < iterable > if < condition >]
squares = [x*x for x in [1,2,3,4,5,6,7]]
print(squares)
print([s.upper() for s in "hello world"])
# print([x for x in 'apple' if x in 'aeiou' else '*'])
print([x if x in 'aeiou' else '*' for x in 'apple'])