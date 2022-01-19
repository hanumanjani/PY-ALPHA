from operator import add
a = add(5676,5747)
print(a, f" --> this is the sum of 5676 and 5747")

from operator import mul
b = mul(465,746775)
print(b, "----->this is multiplication of 465 and 746775")

# MATHODCALLER

alist = ['wolf', 'sheep', 'duck']
c = list(filter(lambda x: x.startswith('d'), alist))
print(c)

from operator import methodcaller

print(list(filter(methodcaller('startswith', 'd'), alist)) )