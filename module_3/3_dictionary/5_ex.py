#def cube_finder(n):
 #   for i in range(1, n+1):
#        print(f"{i}:{i**3}")


#cube_finder(10)

def cube_finder(n):
    d= {}
    for i in range(1,n+1):
        d[i] =i**3
    return d
print(cube_finder(20))