
def func():
    """this function does nothing"""
    return
print(func.__doc__)
help(func())
def greet(name ,greeting='hello'):
    """print a greeting msg to a user"""
    print("{} {}".format(greeting, name))
    return
help(greet)

def hello(name):
    """greet someone .
    print a greeting msg using hello
    """
    print("hello"+name)
    return
class greeter:
    """
    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    hello in this expensive world
    welcome all coder
    hope all are happy and fine
    welcome to python
    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    """
hello('\nhanuman')