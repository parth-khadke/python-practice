x= int(input("Enter a number: "))
y= int(input("Enter a number: "))
z= int(input("Enter a number: "))

if x==y==z:
    print("All numbers are equal.")
elif x>=y and x>=z:
    print("The largest number is ",x)
elif y>x and y>z:
    print("The largest number is ",y)
else:
    print("The largest number is ",z)