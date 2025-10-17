class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance+=amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit to Increase your account balance")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Enter a amount above 100 rupees .")
        else:
            self.balance-=amount
            print(f"Withdrew {amount}. Remaining balance: {self.balance}")

    def display_account(self):
        print()
        print("Your Account Details")
        print("Account Number:",self.account_number,"Owner:",self.owner,"Balance:",self.balance)



account1 = BankAccount(
    int(input("Enter a Account Number")),
    input("Enter Your Name"),
    int(input("Add your Balance")))
account1.display_account()

account1.deposit(500)
account1.withdraw(200)
account1.withdraw(1500) 
account1.display_account()
