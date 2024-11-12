

# class Circle:
#     def __init__(self,radius,pi):
#         self.radius= radius
#         self.pi = pi

#     def calc_circumference(self):
#         return 2*self.pi*self.radius
    
# c1 = Circle(6,3.14)
# c2 = Circle(10,3.14)

# print(c1.calc_circumference())

# print(c2.calc_circumference())




# defining class variable


class Circle:
    pi = 3.14159  # Assign a value to the class attribute

    def __init__(self, radius):
        self.radius = radius

    def calc_circumference(self):
        return 2 * Circle.pi * self.radius  # Use the class attribute pi

c1 = Circle(6)
c2 = Circle(10)

print(c1.calc_circumference())  # Expected: 2 * 3.14159 * 6 = 37.69908
print(c2.calc_circumference())  # Expected: 2 * 3.14159 * 10 = 62.8318



#count instance




class Circle:
    count_instance = 0  # Class attribute to count instances
    pi = 3.14159  # Assign a value to the class attribute

    def __init__(self, radius):
        Circle.count_instance += 1  # Increment the instance count
        self.radius = radius

    def calc_circumference(self):
        return 2 * Circle.pi * self.radius  # Use the class attribute pi

c1 = Circle(6)
c2 = Circle(10)
c3 = Circle(100)

print(Circle.count_instance)  # Access the class attribute without parentheses

