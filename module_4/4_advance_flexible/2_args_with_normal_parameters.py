# * args with normal parameters

# def multiply_nums(*args):
#     print(args)
#     print(type(args))
#     multi = 1
#     for i in args:
#         multi *= i
#     return multi

# print(multiply_nums(1,2,3,4,5))


def multiply_nums(num1,num2,*args):  # we cant give assign values after args, we can do it before args as parameter
    print(args)
    print(type(args))
    multi = 1
    for i in args:
        multi *= i
    return multi

print(multiply_nums(1,2,3,4,5))

