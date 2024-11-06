#list is mutable

#3 ways to add the elements
#append method
#insert method
#extend (method)

fruits=[]
fruits.append("custard apple")
fruits.append(100)
fruits.append(["mango",150])



print(fruits)
print(fruits[2][1])


#insert : positionalway 
fruits.insert(1,"apple")
print(fruits)

print("extend method")

fruits.extend(["dragon fruit",100])
print(fruits)

new_fruit=["papaya",89]
print(fruits+new_fruit)