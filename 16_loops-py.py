i = 0
while i < 7 :
    print(i)
    if i == 4:
        print("braking from the loop")
        break
    i = i+1

for i in (0,1,2,3,4,5):
    print(i)
    if i == 2:
        break

for i in range(12):
    print(i)
for x in [1, 2]:
    print(x)
for index, item in enumerate(['one','two','three']):
    print(index,'::',item)


x = map(lambda e: e.upper(), ['one','two','three'])
print(list(x))

# section 16.6 iterating over dictionaries
d = {"a":1,"b":2,"c":3}
for key in d:
    print(key)

for key in d.keys():
    print(key)

for key, value in d.items():
    print(key, value)