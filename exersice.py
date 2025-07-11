#Create a new class Phone
class Phone():
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    #Accessor methods
    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_price(self):
        return self.price

    def get_info(self):
        return f"Brand: {self.brand} {self.model}, Price: {self.price} $"

    #Mutator method
    def another_info(self, new_brand, new_model, new_price):
        self.brand = new_brand
        self.model = new_model
        self.price = new_price



#Examples:
my_phone = Phone("Samsung", "S24 Ultra", 700)
print(my_phone.get_info())

my_phone.another_info("Iphone", "16 Pro Max", 1000)
print(my_phone.get_info())