import json
d = {
    'foo' : 'bar',
    'harry': 'teacher',
    'hanuman': 'studennt',
     'a':1
}
print(json.dumps(d,indent=2))
with open('2022_json.txt', 'w') as f:
    json.dump(d, f,indent=2)

obj1 = {
    'banana':'574875kg',
    'mango':'4843kg',
    'jdjfjfd':87538753854839573423975343019827385473890132843758,
    'hr':'coader'

}
with open('2022_json2.txt','w') as  f:
    json.dump(obj1,f,indent=2)


with open('2022_json2.txt', 'r') as  f:
    d = json.load(f)
print(d)

