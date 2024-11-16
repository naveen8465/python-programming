class Phone:
    def make_a_call(self,phone_number):
        return f"calling ..... {phone_number}"
    
class Smart_phone:
    def make_a_call(self,phone_number):
        return f"calling ..... {phone_number}"
    

p1 = Phone()
s1 = Smart_phone()

print(p1.make_a_call(108))
print(s1.make_a_call(898383938))