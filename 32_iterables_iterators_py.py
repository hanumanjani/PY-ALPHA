# # CHAPTER - 32 :ITERABLES AND ITERATOR
# class myiterable :
#     def __iter__(self):
#         return self
#     def __next__(self):
#         #code
# # Classic iterable object in older versions of python, __getitem__ is still supported...
#
# # class mysequence:
# #     def __getitem__(self, item):
# #         if ('condition')
# #             raise IndexError
# #         return (item)
#
# #Can produce a plain `iterator` instance by using iter(MySequence())
#
# # import collections
# # collections.Iterator()
# # EXTRACT VALUE ONE BY ONE BY ONE
# s = {1,2, 4, 5}
# i = iter(s)
# a = next(i)
# print(a)
s = {1, 2, 3, 4}
i = iter(s)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
# print(next(i))
for a in s:
    print(a)

print(list(s))
l2 = [a*2 for a in s if a > 2]
print(l2)
d1 = {1 : 'a1', 2 : 'a2', 3 : 'a3', 4 : 'a4'}
for keys, item in d1.items():
    print(keys, '::', item)






