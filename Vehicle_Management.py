class Vehicle:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_details(self):
        print("---- Vehicle Details ----")
        print(f"Brand : {self.brand}")
        print(f"Model : {self.model}")
        print(f"Price :{self.price}")

    def calculate_price(self):
        print("Original Price: ₹", self.price)

class Car(Vehicle):
    def __init__(self, brand, model, price, doors):
        super().__init__(brand, model, price)
        self.number_of_doors = doors

    def display_car_details(self):
        print("---- Car Details ----")
        print(f"Brand : {self.brand}")
        print(f"Model : {self.model}")
        print(f"Price : ₹{self.price}")
        print(f"Number of Doors: {self.number_of_doors}")

tesla = Car("Tesla", 'S', "70.00 Lakh", 4)
tesla.display_details()
tesla.calculate_price()
tesla.display_car_details()