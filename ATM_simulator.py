print("*** ATM SIMULATOR ***")
balance= 1000
exit=0
while exit!=1:
    print("Choose one of the following option: ")
    print("1. Withdraw money")
    print("2. Deposit money")
    print("3. Check Balance")
    print("4. EXIT")
    choice=int(input("Enter your choice digit: "))
    if choice==1 :
        withdraw_amount=int(input("How much do you want to withdraw? :"))
        if withdraw_amount > balance:
            print("Insuffiecient Funds!!")
        else:
            print("Withdraw successful!!")
            balance= balance-withdraw_amount
        print("Remaining Balance: $", balance)
        print()
    elif choice==2:
        deposit=int(input("Enter deposit amount: $"))
        balance= balance+deposit
        print("Current Balance: $", balance)
        print()
    elif choice==3:
        print("Your account balance is: $", balance)
        print()
    elif choice==4:
        exit+=1
    
print("Thank you for using our ATM simulator")