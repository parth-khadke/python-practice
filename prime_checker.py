print()
print("*** Prime Number Checker ***")

while exit!=1:
    number=int(input("Enter a number to check if it is prime: "))
    if number == 1:
        print(f"{number} is not prime")
    elif number>1:
        is_prime= True
        for i in range(2,number):
            if number%i==0:
                is_prime=False
                break
        if is_prime==True:
            print(f"{number} is prime")
        else:
            print(f"{number} is not prime")

        
    choice=input("Do you want to check for another number(y/n): ")
    if choice=='n':
        exit=1
    elif choice=='y':
        continue