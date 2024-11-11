#create your first generator with generator funtion

# 1 generator function
# 2 generator comprehension

# 10 ,1 to 10

# def value_print(n):
#     for i in range(1,n+1):
#         yield i

# print(tuple(value_print(10)))


# for i in value_print(10):
#     print(i)

# def square(n):
#     return n ** 2

# l = [5,4,3,2,1]
# print(tuple(map(lambda a : a ** 2, l)))



# generator comprehension
# l = (i ** 2 for i in range ( 1, 11))
# print(tuple(l))


def gene(n):
    # e= []
    for i in range(1,  n+1):
        if i % 2 == 0:
            yield i


# print(list(gene(20)))
for i in gene(20):
    print(i)

    
