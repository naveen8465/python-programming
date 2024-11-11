

def square(n):
    '''closure property'''
    return n ** 2

# s = square(10)

# print(s)

def outer():
    print("it is outer function")
    def inner():
        print("it is inner function")
    return inner

# f = outer()

# print(f())

def to_power(x):
    def calc_power(y):
        return y ** x
    return calc_power

cube = to_power(3)


square = to_power(2)
print(square(10)) 

