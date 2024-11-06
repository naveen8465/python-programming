fruits=['custard apple', 'apple', 100, ['mango', 150], 'dragon fruit', 100, 'papaya', 89]

#delete way: pop method, remove method, del operator (keyword) 

fruits.pop()
print(fruits)

fruits.remove("apple")
print(fruits)

del fruits[3]
print(fruits)

del fruits[2][0]
print(fruits)