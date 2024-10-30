import random

# class BankAccount:
#     pass

# account_1 = BankAccount()
# account_2 = BankAccount()
# account_3 = BankAccount()
# account_4 = BankAccount()
# account_5 = BankAccount()

class BankAccount:
    def __init__(self, name):
        self.full_name = name
        self.account_number = random.randint(10000000, 99999999)
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

    def get_balance(self):
        print(f"Your current balance is: ${self.balance}.")
        return self.balance

    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance += interest
        self.balance = round(self.balance, 2)
        print(f"Your current monthly balance (with interest) is {interest}.")
        return interest

    def print_statement(self):
        print(f"{self.full_name}\nAccount No.:{self.account_number}\nBalance: ${self.balance}")

#3 Different Bank Accounts:

#1 Mitchell Hudson
print("\n")
user_mitchell = BankAccount("Mitchell Hudson")
user_mitchell.deposit(400000)
user_mitchell.withdraw(150)
user_mitchell.get_balance()
user_mitchell.add_interest()
user_mitchell.print_statement()
print("\n")

#2 Christopher Bang

user_chris = BankAccount("Chris Bang")
user_chris.deposit(8002300)
user_chris.withdraw(230)
user_chris.get_balance()
user_chris.add_interest()
user_chris.print_statement()
print("\n")

#3 Jane Fernandez

user_jane = BankAccount("Jane Fernandez")
user_jane.deposit(7109207)
user_jane.withdraw(207)
user_jane.get_balance()
user_jane.add_interest()
user_jane.print_statement()
print("\n")
