string=input("Enter a string to check if palindrome: ")
string=string.lower()
reversed_string=string[::-1]

if string==reversed_string:
    print(" The string is a palindrome.")
else:
    print("String is not a palindrome.")