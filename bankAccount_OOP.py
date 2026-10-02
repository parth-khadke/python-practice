class BankAccount:

    def __init__(self, acc_num, acc_hol, bal):
        self.acc_number = acc_num
        self.acc_holder = acc_hol
        self.balance = bal

    def CheckBalance(self):
        return self.balance

    
    def deposit(self, amt):
        if amt <= 0:
            print("Deposit Amount must be greater than 0 . Try again")
        else:
            self.balance += amt
            print("Deposit Successful")
            new_bal = self.CheckBalance()
            print("Current Balance :", new_bal)


    def withdraw(self, amt):
        if amt<= 0 :
           print("Witdhraw Amount must be greater than 0 . Try again")
        elif self.balance < amt:
           print("Insufficient Balance")
        else:
            self.balance -= amt
            print(f"Withdraw Amount {amt} . Succesful")
            curr_bal = self.CheckBalance()
            print("Current Balance:", curr_bal)


    def display_acc_details(self):
        print("Account Details : ")
        print("Account Number: ",self.acc_number)
        print("Account holder: ",self.acc_holder)
        print("Account balance: ",self.balance)


acc1 = BankAccount(10001, "Parth", 10000)

# acc1.display_acc_details()

acc1.deposit(12345)

acc1.display_acc_details()

acc1.withdraw(9000)

acc1.CheckBalance()
