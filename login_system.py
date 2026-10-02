print("*** LOGIN SYSTEM ***")

for i in range(3):
    id=input("Enter ID: ")
    password=input("Enter Password: ")
    access=False
    if id == "admin" and password== "1234":
        access=True
        print("Welcome!!")
        break
    else:
        print("Invalid Credentials!!!\n TRY AGAIN \n")

if access==False:
    print("You are locked out.")
