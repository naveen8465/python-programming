#iterator vs iterable

num = list(range(1,11)) #iterable

mun= map(lambda a : a ** 2, num)#iterator

print(mun)

# for i in range(1,5):
#     print(i)

# 1- it will call -- iter()
# 2- iter(numbers)-- iterator -- object
# 3- next(iter (numbers))

num = list(range(1,11)) #iterable
a= iter(num)

print(next(a))
print(next(a))
print(next(a))
print(next(a))

