l = [1,2,3,4,5,]

l1= list(range(1,101))
print(l1)

def neg_list(n):
    e=[]
    for i in n:
        e.append(-i)
    return e
    
print(neg_list(l1))
print(neg_list(l))