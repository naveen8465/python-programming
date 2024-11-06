#user moretghan 1 digit number

#10 - 1+2+3+4+....10

#99 - 9+9
#2002 - 2+0+0+2

#n, i , total, while

n=input("enter a num to be sum of digits must give more than a digit: ")


total = 0
#i=0
#9999 = 9+9+9+9 = 36
#while i < len(n):
    #len(9999) = 4
   # total += int(n[i])
   # i +=1
#print(total)

#for i in range (len(n)):
   # total += int(n[i])
    #print(total)

for i in n:
    total += int(i)
    print(total)

    

    #case1 : i=0 , t= 0
    #t=0+9 = 9

    #case 2: i=2, t=9
    #t=9+9 = 18

    #case 3: i = 3, t= 9
    #t=18+9 = 27

    #case 4: i=4, t= 9
    #t=27+9 =36

    #case 5: i=5, t=9
    #t=36+9 = 45
