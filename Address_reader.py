print("*** Address Reader ***")
address = input("Enter you full adress: ")
house_no, street, city, state, zip_code = address.split(", ")
print("Address:\n{}, {},\n{}, {},\n{}".format(house_no, street, city, state, zip_code))
