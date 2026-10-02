x = int(input("Enter the first number(x): "))
y = int(input("Enter the second number(y): "))

if x<y:
    print("Quotient of y/x: ", y/x)
    print("Remainder of y/x: ", y%x)
elif y<x:
    print("Quotient of x/y: ", x/y)
    print("Remainder of x/y: ", x%y)
elif x==y:
    print("Numbers are equal. Quotient = 1, remainder = 0")
