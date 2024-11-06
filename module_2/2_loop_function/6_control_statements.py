#control statements- break, continue, pass 

#for i in range(5):
 #   if i == 2:
   #     pass
   # print(i)

#for i in range(5):
#        if i == 2:
 #               continue
 #   print(i)

for i in range(10, 16):
    if i == 8:  # Since i starts at 10, this will never trigger
        break
    elif i == 13:
        continue
    else:
        print("hyderabad")
    
    print(i)  # This will print the value of i in all cases except when i == 13
    print("delhi")

