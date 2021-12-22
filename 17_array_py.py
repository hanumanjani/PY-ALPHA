from array import *
arr = array('i', [1, 2, 3, 4, 5, 6, 7])
for i in arr :
    print(i, "--->", {i})


# APPEND
arr.append(8)
print(arr)

# INSERT
arr.insert(0, 0)
print(arr)
arr.insert(3, 99)
print(arr)

# EXTEND ARRAY
arr1 = array('i', [12, 13, 14])
arr.extend(arr1)
print(arr)
c = [1,2,3]
arr.fromlist(c)
print(arr)
arr.remove(4)
print(arr)
print(arr.index(99))
print(arr.index(2))
# print(arr.buffer_info())
print(arr.count(1))
# print(arr.tostring())
# arr.tostring()
# print(arr)
print(arr.tolist())
print(arr)
# arr2 = array('c', ['j', 'k', 'l'])
# print(arr2.tostring())
# my_char_array = array('c', ['g', 'e', 'e', 'k'])
# my_char_array.fromstring("stuff")
# print(my_char_array)


