def sup_sert_fn(f):
    print("hey!")
    return f

@sup_sert_fn
def fun1():
    print("this is mysecretfunction")

fun1()

def disabled(f):
    """
    this function return nothing,
    and hence removes the decorated function
    fron local scope
    :param f:
    :return:
    """
    pass
@disabled
def my_fun1():
    print("this function no longer called .......")

print(my_fun1)

def print_args(func):
    def inner_fun(*args, **kwargs):
        print(args)
        print(kwargs)
        return func(*args,**kwargs)
    return inner_fun
@print_args
def multiply(a,b):
    return a*b
print(multiply(3,5))

#Output:
# (3,5) - This is actually the 'args' that the function receives.
# {} - This is the 'kwargs', empty because we didn't specify keyword arguments.
# 15 - The result of the function.

# DECORATOR CLASS

# class Decorator(object):
#     """simple decorator class"""
#     def __init__(self,func):
#         self.func = func
#     def __ceil__(self,*args,**kwargs):
#         print('before the function call...')
#         res = self.func(*args,**kwargs)
#         print('after the function call..')
#         return res
# @ Decorator
# def testfn():
#     print('inside the function.......')
#
#
# testfn()

