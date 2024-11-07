#dict comp with if else

def odd_even(n):
    d={}
    for i in n:
        if n[i] > 0:
            if i%2 == 0:
               d[i]= "even"
            else:
               d[i]= "odd"
    return d

d= {i : "even" if i % 2 == 0 else  "odd" for i in list(range(1,15))}
# print(odd_even(list(range(15))))

print(d)


