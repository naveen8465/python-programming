#lambda function
#anonymous function

# def add(a,b):
#     return (a+b)

# print(add(5,4))

# l= lambda a,b :(a+b)

# print(l(4,5))

# def odd_even(a):
#     if a% 2 == 0:
#         return True
#     else:
#         False
# print(odd_even(50))

# c =lambda a : a % 2 == 0
# print(c(9))

# def last_val(a):
#     return a[-1]

# print(last_val("naveen"))

# s = lambda a: a[-1]

# print(s("chandu"))

def fun(s):
    if len(s) > 5:
        return True
    return False

print(fun("naveen"))

length = lambda y : len(y) > 5

print(length("yamuna"))