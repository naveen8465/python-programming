#decorators - extra functionality
#it will enhance the functionality of other function

from functools import wraps


def decorator_function(any_function):
    @wraps(any_function)
    def wrapper_function(*args,**kwargs):
        print("this is with makeup")
        return any_function(*args,**kwargs)
    return wrapper_function

@decorator_function
def add(a,b):
    '''it is add function'''
    return a+b

# print(add(2,5))
print(add.__doc__)
print(add.__name__)
