password=input("Enter you password: ")

if len(password)<6:
    print("Weak Passoword")
elif 6< len(password) <10 and password.isalpha():
    print("Medium Strength")
elif len(password)>=10 and password.isalnum:
    print("Strong")
