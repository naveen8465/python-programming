#flexble functions--- * --- args,---- ** kwargs 

# def square(*n):
#     l=[]
#     for i in n:
#         l.append(i**2)
#     return l


# print(square(1,2,3))


def total(a,b):
    return a+b

# print(total(5,54))

# def alllll(*args):
#     print(args)
#     print(type(args))

# alllll("naveen")

# alllll("naveen","praveen","kaveen")

def alllll(*args):
    total= 0
    for i in args:
        total += i
    return total

print(alllll(1,2,3,4,5))

