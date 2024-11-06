#using udf of list reverse every element
#['abc','cde']

def rev_element(n):
    e=[]
    for i in n:
        e.append(i[::-1])
    return e
l = ["abc","cde"]
print(rev_element(l))