

class Person:

    count_instance = 0

    def __init__(self, first_name, last_name, age):
        Person.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = int(age)  # Convert age to integer

    @classmethod
    def class_constructor(cls, string):
        first, last, age = string.split(',')  # Fix the typo in split
        return cls(first, last, age)
    @staticmethod
    def hello():
        return "hello, static method called"

    @classmethod
    def count(cls):
        return f"You have created {cls.count_instance} instances"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def is_above_18(self):
        return self.age > 18

# Create instances
p1 = Person("naveen", "jakki", 24)
p2 = Person("chandu", "vadde", 28)

# Access instance methods and class methods
print(p1.full_name())           # Expected: "naveen jakki"
print(p1.is_above_18())         # Expected: True

# Class method
print(Person.count())           # Expected: "You have created 2 instances"

# Using class constructor
c1 = Person.class_constructor("khammam,mudigonda,30")  # Pass a single string
print(c1.full_name())          # Expected: "khammam mudigonda"
print(c1.is_above_18())        # Expected: True

print(p1.hello())


