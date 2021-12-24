


# def func(arg1, arg2=10, **kwargs):
#  try:
#  kwarg1 = kwargs.pop("kwarg1")
#  except KeyError:
#  raise TypeError("missing required keyword-only argument: 'kwarg1'")
#  kwarg2 = kwargs.pop("kwarg2", 2)
#  # function body ...




# LAMBDA FUNCTION--->

gree_tme = lambda: print('hello! -> -> -> ')
print(gree_tme())
gree_tme()

# lambda function can take argument
strip_and_upper_case = lambda s: s.strip().upper()
print(strip_and_upper_case("hello!"))
hghdfjs = lambda a, b, c: print(a,b,c)
hghdfjs(1, 2, 'hanuman')
def func1(a, b = 42,c=[]):
    pass
print(func1.__defaults__)


def append(elem,to=[]):
    to.append(elem)
    return to
print(append(12))
print(append(114))
def f(a, b, c):
    pass
print(f(1,2,3))

# recursuon
def cursing(depth):
 try:
      cursing(depth + 1) # actually, re-cursing
 except RuntimeError as RE:
    print('I recursed {} times!'.format(depth))
cursing(0)
print(225/856*100)





