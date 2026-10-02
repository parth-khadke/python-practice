import math
l = int(input("Enter the length of the rectangle: "))
b = int(input("ENter the breadth of the rectangle: "))

exit=0
while (exit==0):
    print("1. Perimeter")
    print("2. Area")
    print("3. Diagonal")

    choice=int(input("Choose one of the options: "))

    if choice==1:
        perimeter=2*(l+b)
        print("Perimeter of the rectangle is ", perimeter)
    elif choice==2:
        area=l*b
        print("Area of the rectangle is ", area)
    elif choice==3:
        diagonal=(l*l)+(b*b)
        diagonal=math.sqrt(diagonal)
        print("The diagonals of the rectangle is ", diagonal)
    elif choice==0:
        print("THANK YOU FOR USING THIS PROGRAM!!")
        break