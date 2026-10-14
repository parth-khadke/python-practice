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
        

restaurant = Restaurant("Olive Garden", "Continental")

print(restaurant.describe_restaurant())
print(restaurant.open_restaurant())

print(restaurant.number_served)

restaurant.set_number_served(25)
print(restaurant.number_served)

restaurant.increment_number_served(5)
print(restaurant.number_served)

