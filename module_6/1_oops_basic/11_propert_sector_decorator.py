class Phone:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
        self.complete_spec = f"{self.brand} {self.model} and the price is {self.price}"
    

    def make_a_call(self,phone_number):
        return (f"calling .... {phone_number}")
    
    def full_name(self):
        return f"{self.brand_name} {self.model_name}"
    

p1 = Phone("samsung","A1", 1000)

p1.price= 500
print(p1.price)

print(p1.complete_spec)