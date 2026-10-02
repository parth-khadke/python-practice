class Product:
    def __init__(self, name, price, quant):
        self.prod_name = name
        self.__prod_price = price
        self.__quantity = quant

    def get_Price(self):
        return self.__prod_price

    def set_Price(self, price):
        self.__prod_price = price

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, qtt):
        self.__quantity = qtt

    def calculate_total(self):
        total_price = self.__prod_price * self.__quantity
        print("total price : ₹", total_price)

class Electronics(Product):
    def __init__(self, name, price, quant, brand, warranty):
        super().__init__(name, price, quant)
        self.brand = brand
        self.warranty = warranty

    def display_details(self):
        print("----Product Details----")
        print(f"Product Name : {self.prod_name}")
        print(f"Product Price : {self.get_Price()}")
        print(f"Quantity : {self.get_quantity()}")
        print(f"Brand : {self.brand}")
        print(f"warranty : {self.warranty}")

    def calculate_total(self):
        entc_service_charge = 10
        price = self.get_Price()
        quantity = self.get_quantity()
        additional_charge = (price * quantity) * entc_service_charge/100
        total = (price * quantity) + additional_charge
        print("total price : ₹", total)

    

        
        