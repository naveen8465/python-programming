matrix = [[1,2,3],[1,4,9],[1,8,18]]

for i in matrix:
    print(i)

for i in matrix:
    for j in i:
        print(j)

for i in matrix:
    for j in i:
        print(j, end=" ")
        