# create dict to represent product details

prod_dict = {'name': "iphone", "price":80000, "category": "electronic"}

# create a dict to represent course details

course_dict = {"crs-name": "Python", "Duration": 5, "Fees": 40000, 'Faculty': "Vaibhav Sir"}

# for loop

# for key in course_dict:
#     print(f"'{key}' : {course_dict[key]}")

# for i in course_dict.values():
#     print(i)

# for i,j in course_dict.items():
#     print(f"'{i}' : {j}")
    
string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."

print(string.capitalize())
print(string.count("e"))
print(string.upper())
print(string.lower())
print(string.casefold())
print(string.replace("may", "hello"))
# print(string.encode('ASCII'))
print(string.isdigit())
print(string.split(sep='i'))
