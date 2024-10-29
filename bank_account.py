import random

class BankAccount:
    pass

account_1 = BankAccount()
account_2 = BankAccount()
account_3 = BankAccount()
account_4 = BankAccount()
account_5 = BankAccount()

class BankAccount:
    def __init__(self, name, account, balance):
        self.full_name = name
        self.account_number = account
        self.balance = 0

def deposit(self, amount):
    self.balance += amount
    print(f"Amount deposited: ${amount} | New balance: ${self.balance}")

def withdraw(self, amount):
    self.balance -= amount
    if self.balance < 0:
        print("Insufficient funds. You will now be charged with an overdraft fee of $10.")
        self.balance -= 10
    else:
        print(f"Amount withdrawn: ${amount} | New balance: ${self.balance}")



    

