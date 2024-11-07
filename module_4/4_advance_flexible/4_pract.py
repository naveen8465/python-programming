



def to_do(n,*args):
    l=[]
    for i in args:
        l.append(i**n)
    return l

l=[1,2,3,4,]
print(to_do(2,*l))

n=2
print([i**n for i in l])