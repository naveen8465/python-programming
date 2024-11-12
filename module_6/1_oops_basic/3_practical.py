#create a laptop class with attribute like brand name,model name, proice

#create the objects/instance of your laptop class


class Laptop:
    count = 0
    discount_percent= 21
    def __init__(self, brand_name, model_name, price):
        Laptop.count +=1
        self.brand_name= brand_name
        self.model_name = model_name
        self.price = price

    def apply_discount(self):
        off_price = (self.discount_percent/100)*self.price
        return self.price - off_price


l1 = Laptop("lenovo","idea pad",60000)
l2 = Laptop("asus","vivobook 15",45000)
l3 = Laptop("dell","lattude",50000)
l4 = Laptop("hp","victus", 90000)

print(l1.apply_discount())
print(l3.apply_discount())
print(l4.apply_discount())
print(l2.apply_discount())

print(Laptop.count)