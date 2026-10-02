student = ("Arjun", 21 , "Computer Science")

#print("Name: ", student[0])
#print("Age: ", student[1])
#print("Branch: ", student[2])


products = ("Keyboard", 2499, 15)
product, price, stock = products

#print(f"{name} costs ₹{price} and {stock} units are available") 

movies = (
    "Interstellar",
    "Inception",
    "The Dark Knight",
    "Oppenheimer",
    "Tenet"
)

first, *middle, last = movies

#print(first, middle, last)

sales = (120, 150, 180, 200, 170, 220)
month = 1
for i in sales:
 #   print(f" Month {month}: {i}")
    month+=1

#print("Total Sales: ", sum(sales))
#print("Highest Sale: ", max(sales))

employee = (101, "Alice", "Developer", 85000)

emp_id, name, role, salary = employee

print(f"Employee ID: {emp_id}\nName: {name}, \nRole : {role},\nSalary: {salary}")
