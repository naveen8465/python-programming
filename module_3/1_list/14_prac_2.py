#filter odd and even 
#define a function
#input
#list   [1,2,3,4,5,6,7,8,9]

def odd_even(n):
    o=[]
    e=[]
    for i in n:
        if i % 2== 0:
            e.append(i)
        else:
            o.append(i)
    return o,e
i = [1,2,3,4,5,6,7,8,9]
print(odd_even(i))