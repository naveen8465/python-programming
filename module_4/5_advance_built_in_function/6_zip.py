a = ["high","junior","railway","police"]

b = ["school","college","line","station"]

# print(list(zip(a,b)))

print(dict(zip(a,b)))

# task 

def avg_finder(l1,l2,l3):
    e=[]
    for i in zip(l1,l2,l3):
        e.append(sum(i)/len(i))
    return e


print(avg_finder([1,2,3],[4,5,6],[7,8,9]))