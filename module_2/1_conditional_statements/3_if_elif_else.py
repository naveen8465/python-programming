#more than one condition is true 

#0-3 years no ticket
#3-10 years half ticket
#10-55 years full ticket
#greater than 55 senior citizen ticket

age =int(input("enter your age:"))

if age > 0 and age <= 3:
    print("no ticket")
elif age > 3 and age <= 10: 
    print("half ticket")
elif age > 10 and age <= 55:
    print("full ticket")
elif age > 55:
    print("senior citizen ticket")
else:
    print("please enter a valid age")