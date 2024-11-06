#sum of n numbers

#sum of 10 numbers = 1+2+3+4+.....10 = 55

n=int(input("enter a number:"))
#i= 0
#total = 0
#while i <= n:
   # total += i
    #print(total)
    #i += 1

f_total = 0
for i in range(1, n+1):
    f_total += i
    print(f_total)



    #case 1: i=1, t=0
    #t=0+1 = 1

    #case 2 : i=2, t=1
    #t=1+2 =3

    #case 3: i=3, t=3
    #t=3+3 = 6

    #case 4: i=4, t=6
    #t= 6+4 = 10

    #case5: i = 5, t= 10
    #t= 10+5 = 15

