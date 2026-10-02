""" print("Welcome to python batch")
print(78)
clas= "CSR"
name = "Parth Khadke"
print( name, clas, sep="  !!!  " )
city="Pune"
print(city)
print("course") """


# length= int(input("length :"))
# width = int(input("width :"))

# # area =  base * height

# diagonal = ((length**2) + (width**2))**0.5
# print("diagonal: ", diagonal)


""" 
name = input("Enter your name: ")

print("My name is",name)
 """

# num = int(input("Enter a number: "))
# print(num)
# print(type(num))
# # square = num**2
# # print("Square :", num**2)

""" MRP = eval(input("MRP: "))
disc = float(input("Enter Discout: "))
sell_price = MRP - (MRP*(disc/100))
print(sell_price) """

# string formatting
""" 
name = "Parth Khadke"
course= "Python"
duration = "3 months"

print("My name is {}, \nCourse : {}, \nDuration: {}".format(name, course, duration))
 """

""" 
product = input("Enter Product name: ")
prod_category = input("Enter Category: ")
prod_price = eval(input("Enter Price : "))

# print("\nProduct Name : {}, \nProduct Category : {}, \n MRP : ₹{}".format(product, prod_category, prod_price))
print(f"Product Name : {product}, \nProduct Category : {prod_category}, \nMRP : {prod_price}") """

# create email ---> fname_lastname@companyname.com

fname = input("ENter first name : ")
last_name = input("ENter last name : ")
company_name = input("ENter company name : ")

print(f"{fname}_{last_name}@{company_name}.com")
