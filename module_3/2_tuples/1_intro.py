#tuple any type of data we can store


example= ("naveen", "bhargav", "Kalyani", ["dhoni", "sachin"])


#example.append("vinod") no append in tuple

#for i in example:
   # print (i.upper())

#tuples are faster than lists

#we can perform slicing
#indexing
#len function also

#for i in example:
 #   if type(i)== list:
 #       i.append("rohit sharma")
#print(example)

#t = (10) #int

#t = (10, 100) #tuple

#print(type(t))

#l =[10]
#print(type(l))

#tuple without paranthesis

#name= "naveen","bhargav", "kalyani"

#print(name)

#tuple unpacking
#men_in_blue = ("virat","dhoni","sachin")
#batsman, wk, bowler= (men_in_blue)
#print(batsman)


def odd_even(n):
    o=[]
    e=[]
    for i in n:
        if i % 2 == 0:
            e.append(i**2)
        else:
            o.append(i**3)
    return o,e
    

print(odd_even(list(range(1, 11))))




