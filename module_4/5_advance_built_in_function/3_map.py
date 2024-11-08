# def square(n):
#     e=[]
#     for i in n:
#         e.append(i ** 2)
#     return e

l =[2,3,4,5,]

# print(square(l))
def square(n):
    return n ** 2

m = list(map(square,l))
print(m)
