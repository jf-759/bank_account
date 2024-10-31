import random

class BankAccount:
    def __init__(self, name, account_type):
        self.full_name = name
        self.account_number = random.randint(10000000, 99999999)
        self.balance = 0
        self.account_type = account_type
        self.set_account_type(account_type)

    def display_account_info(self):
        print(f"Account Holder {self.full_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.account_type.capitalize() if self.account_type else 'Not Set'}")
        print(f"Balance: ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount deposited: ${amount} | New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds. You will now be charged with an overdraft fee of $10.")
            self.balance -= 10
        else:
            print(f"Amount withdrawn: ${amount} | New balance: ${self.balance}")

    def get_balance(self):
        print(f"Your current balance is: ${self.balance}.")
        return self.balance

    def add_interest(self, account_type):
    
        interest = self.balance * 0.00083
        self.balance += interest
        self.balance = round(self.balance, 2)
        print(f"Your current monthly balance (with interest) is {interest}.")
        return interest

    def print_statement(self):
        print(f"{self.full_name}\nAccount No.:{self.account_number}\nBalance: ${self.balance}")

#3 Different Bank Accounts (checkings and savings):

#1 Mitchell Hudson
print("\n")

checking1 = BankAccount("Mitchell Hudson")
checking1.deposit(400000)
checking1.withdraw(150)
checking1.get_balance()
checking1.add_interest("checkings")
checking1.print_statement()
checking1.display_account_info()
print("\n")
savings1 = BankAccount("Mitchell Hudson")
savings1.deposit(500000)
savings1.withdraw(200)
savings1.get_balance()
savings1.add_interest("savings")
savings1.print_statement()
savings1.display_account_info()
print("\n")

