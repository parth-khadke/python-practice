class BankAccount():
    def __init__(self, name, balance):
        self.account_holder = name
        self.balance = balance

    def deposit(self, amt):
        if amt <= 0:
            print("Deposits must be greater than 0.")
        else:
            self.balance += amt
            print(f"Deposit Successful")

    def withdraw(self, amt):
        if amt <= 0:
            print("Withdrawal Amount must be greater than zero")
        else:
            if self.balance < amt:
                print("Insuffiecient Funds")
            else:
                self.balance -= amt
                print("Withdraw succesful")

    def checkBalance(self):
        print(f"Available Balance : {self.balance}")


account = BankAccount("Arjun", 500)

account.checkBalance()

account.deposit(500)
account.withdraw(300)
account.withdraw(1500)
account.deposit(-500)

account.checkBalance()