#def list_square(l):
 #   e=[]
 #   for i in l:
 #       e.append(i**2)
 #   return e

#print(list_square(list(range(1,11))))


#lc = [i**2 for i in range(1,11)]
#print(lc)


#condition for loop
#condition for loop if
#condition if else condition for 



#def list_square(l):
#    e=[]
#    for i in l:
 #       if i%2 == 0:
 #           e.append(-i)

#lc = [-i for i in range(1,11) if i %2 == 0]
#print(lc)


# def list_square(l):
#     e=[]
#     for i in l:
#         if i%2 == 0:
#             e.append(-i)
#         else:
#             e.append(i**3)
#     return e


# lc = [-i  if i %2 == 0  else i**3 for i in range(1,11)]
# print(lc)



#reversing the list of [abc , bca, cab]

# def rev(l):
#     e=[]
#     for i in l:
#         e.append(i[::-1])
#     return e

# lc = [i[::-1] for i in ["abc","bca","cab"]]
# print(lc)
# print(rev(["abc","bca","cab"])

#example [[123],[123],[123]]

print([[i for i in range(1,4)] for j in range (4)])