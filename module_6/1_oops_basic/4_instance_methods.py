#instance methods


class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

p1 = Person("naveen", "jakki", 24)
p2 = Person("chandu","vadde", 28)

print(p1.full_name())


print(Person.full_name(p2))

# l = [1,2,3,4]

# l.append(5)

# list.append(l,5)

# print(l)