from enum import Enum
class color(Enum):
    red = 1
    green =2
    blue = 3

print(color.red)
print(color(1))
print(color['red'])
print([c for c in color])