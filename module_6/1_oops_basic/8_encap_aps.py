#encapsulation

#abstruction

#some special naming conventions

#name mangling(__name ) -- is not a convention

#access modifiers -- public ,private _ , protected __

class Phone:
    def __init__(self,brand_name,model_name,price):
        self.brand_name = brand_name
        self.model_name = model_name
        self.__price = price
    

    def make_a_call(self,phone_number):
        return (f"calling .... {phone_number}")
    
    def full_name(self):
        return f"{self.brand_name} {self.model_name}"
    

p1 =Phone("samsung","s21", 150000)

print(p1.__dict__)

# print(p1._Phone__price)

# p1._Phone__price=12000
# print(p1._Phone__price)  - protected __  we have to use __ for protected and we have to use _class__object 



# p1._price = 12000
# print(p1._price) # private is _

    


l = [3,4,2,1,6,5]
l.sort() #abstraction hiding internal details or complexity
print(l)