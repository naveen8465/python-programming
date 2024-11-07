



#cat one file
#touch n number of files


#square key : value **2

# def dict_square(n):
#     d ={}
#     for i in n:
#         d[i] = i**2
#     return d

# l = list(range(1,21))

# print(dict_square(l))



# d={i : i**3 for i in list(range(1,20))}  #condition for loop
# print(d)

#string formatting
# d={f"cube of {i}: is  {i**3}"for i in list(range(1,20))}
# print(d)


# def word_count(n):
#     d={}
#     for i in n:
#         d[i]= n.count(i)
#     return d
# print(word_count("indian army"))

c= "indian army  indian"

print({i:c.count(i) for i in c})
