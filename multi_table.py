print()
print("*** Multiplication Table Generator")
exit=1
while exit!= 0:
    number=int(input("Enter a number between 1-10 for a multiplication table: "))
    if number<1 or number>10:
        print("Enter a valid number")
    else:
        for i in range(1,11):
            print(f"{number} x {i} = {number*i}")
    choice=input("Do you want another table y/n: ")
    if choice=='n':
        exit=0
    elif choice=='y':
        print()
        continue