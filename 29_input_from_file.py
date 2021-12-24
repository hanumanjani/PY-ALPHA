# let's creat a file
with open('shoppinglist.txt', 'w') as fileobj:
    fileobj.write('banana\norange\nmango')

with open('shoppinglist.txt', 'r') as fileobj:
    lines = fileobj.readlines()
    lin1 = fileobj.read()
    line_s = lin1.split('\n')

print(lines)
# line_s = lines.split('\n') --->error
# lin1 = fileobj.read()         --------->error
# line_s = lin1.split('\n')
print(line_s)

# 30 -----------> FILE AND FOLDER--------------------------->>>>>


"""
try:
 with open("fname", "r") as fout:
 # Work with your open file
except FileExistsError:
 # Your error handling goes here
"""
with open('myfile.txt', 'a') as fp:
     fp.write('\n'+input())
with open('myfile.txt','r') as ff:
    for line in ff :
        print(line)


with open('myfile.txt','r') as fb:
    while True:
        cur_line = fb.readline()
        if cur_line == '':
            break
        print(cur_line)