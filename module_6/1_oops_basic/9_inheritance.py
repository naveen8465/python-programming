#method resolution order (MOU)

# l = list(tuple(range(1,11)))# chil and mother relationships

class Phone:
    def __init__(self,brand_name,model_name,price):
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
    

    def make_a_call(self,phone_number):
        return (f"calling .... {phone_number}")
    
    def full_name(self):
        return f"{self.brand_name} {self.model_name}"
    
class Smart_phone(Phone):
    def __init__(self,brand_name,model_name,price,ram,internal_memory,rear_camera):
       # Phone.__init__(self, brand_name,model_name,price)
        super().__init__(brand_name,model_name,price)
        # self.brand_name = brand_name
        # self.model_name = model_name
        # self.price = price
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

    # def make_a_call(self,phone_number):
    #     return (f"calling .... {phone_number}")
    
    # def full_name(self):
    #     return f"{self.brand_name} {self.model_name}"
    
    
    

p1 = Phone("samsung","guru",11000)
p2 = Phone("nokia","a1",9000)
p3 = Phone("motorola","m5",8000)

s1 = Smart_phone("samsung","s24",11000,"16gb","512gb","108mp")
s2 = Smart_phone("Apple","15",150000,"12gb","256gb","32mp")
s3 = Smart_phone("motorola","m35",35000,"8gb","256gb","48mp")


# print(p1.full_name())
# print(s1.full_name())
# print(p1.make_a_call(1234567890))
# print(s1.make_a_call(988766534))

# print(help(Phone))
print(help(Smart_phone))
