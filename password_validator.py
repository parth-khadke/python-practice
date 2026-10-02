print("*** Password Validator ***")

while True:
    password = input("Enter your password: ")
    
    # Check length
    if len(password) < 8:
        print("Password too short (minimum 8 characters)")
        continue
    
    # Check for at least one digit
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break  # Found one, no need to check rest
    
    if not has_digit:
        print("Password must contain at least one digit")
        continue
    
    # If we get here, password is valid
    print("Valid password!")
    break