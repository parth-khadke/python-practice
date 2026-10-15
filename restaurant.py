class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0 

    def describe_restaurant(self):
        return f"Restaurant is {self.name}.\nIt serves {self.cuisine_type} food"


    def open_restaurant(self):
        return "Restaurant is now open"

    def set_number_served(self, num):
        if num>= self.number_served:
            self.number_served = num
            return f"{self.number_served} customers served"
        else:
            return "Cannot lower the number"

    def increment_number_served(self, count):
        self.number_served += count
        

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["Vanilla", "Butterscotch", "Strawberry", "Lotus Biscoff", "Pista"]

    def ShowFlavors(self):
        print('Available Flavors:')
        for i in self.flavors:
            print(i, end=", ")

    
IceCreamParlour = IceCreamStand("Perfect Cold", "Ice Cream")

IceCreamParlour.ShowFlavors()