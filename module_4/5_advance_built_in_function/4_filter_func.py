#filter function

# def odd_even(n):
#     e=[]
#     for i in n:
#         if i % 2 == 0:
#             e.append(i)
#     return e

l = list(range(1,11))
# print(odd_even(l))

ft = list(filter(lambda a : a % 2 == 0,l))

print(ft)

#task same thing in list comprehension

lc = [ i for i in l if i % 2 == 0]
print(lc)


