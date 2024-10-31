import random

class BankAccount:
    def __init__(self, name, account_type):
        self.full_name = name
        self.account_number = random.randint(10000000, 99999999)
        self.balance = 0
        self.account_type = account_type
        self.set_account_type(account_type)

    def display_account_info(self):
        return (f"Account Holder {self.full_name}\n"
            f"Account Number: {self.account_number}\n"
            f"Account Type: {self.account_type.capitalize() if self.account_type else 'Not Set'}\n"
            f"Balance: ${self.balance}")


    def deposit(self, amount):
        self.balance += amount
        return(f"Amount deposited: ${amount} | New balance: ${self.balance}")

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            self.balance -= 10
            return("Insufficient funds. You will now be charged with an overdraft fee of $10.")
        else:
            return(f"Amount withdrawn: ${amount} | New balance: ${self.balance}")

    def get_balance(self):
        print(f"Your current balance is: ${self.balance}")
        return self.balance

    def add_interest(self):
    
        interest = self.balance * 0.00083
        self.balance += interest
        self.balance = round(self.balance, 2)
        return(f"Your current monthly balance (with interest) is {interest}.")
    
    def set_account_type(self, account_type):
        if account_type == "checkings":
            self.account_type = "checkings"
            self.intterest_rate = 0.00083
        elif account_type == "savings":
            self.account_type = "savings"
            self.intterest_rate = 0.012 / 12
        else:
            raise ValueError("Invalid account type. Please choose either 'checkings' or 'savings'. Thank you.")

    def print_statement(self):
        hidden_account_number = (str(self.account_number)[4:8])
        hidden_account_number = "****" + hidden_account_number
        print("-"*70)
        print(f"{self.full_name}\nAccount No.:{self.account_number}\nBalance: ${self.balance}")
        print("-"*70)

#3 Different Bank Accounts (checkings and savings):

#1 Mitchell Hudson
print("\n")

checking1 = BankAccount("Mitchell Hudson", "checkings")
print(checking1.deposit(400000))
print(checking1.withdraw(150))
print(checking1.get_balance())
print(checking1.add_interest())
print(checking1.print_statement())
print(checking1.display_account_info())

print("\n")

savings1 = BankAccount("Mitchell Hudson", "savings")
print(savings1.deposit(802300))
print(savings1.withdraw(200))
print(savings1.get_balance())
print(savings1.add_interest())
print(savings1.print_statement())
print(savings1.display_account_info())

print("\n")

checking2 = BankAccount("Chris Bang", "checkings")
print(checking2.deposit(801000))
print(checking2.withdraw(300))
print(checking2.get_balance())
print(checking2.add_interest())
print(checking2.print_statement())
print(checking2.display_account_info())

print("\n")

savings2 = BankAccount("Chris Bang", "savings")
print(savings2.deposit(3250000))
print(savings2.withdraw(500))
print(savings2.get_balance())
print(savings2.add_interest())
print(savings2.print_statement())
print(savings2.display_account_info())

print("\n")


checking3 = BankAccount("Jane Fernandez", "checkings")
print(checking3.deposit(700300))
print(checking3.withdraw(300))
print(checking3.get_balance())
print(checking3.add_interest())
print(checking3.print_statement())
print(checking3.display_account_info())

print("\n")

savings3 = BankAccount("Jane Fernandez", "savings")
print(savings3.deposit(759000))
print(savings3.withdraw(100))
print(savings3.get_balance())
print(savings3.add_interest())
print(savings3.print_statement())
print(savings3.display_account_info())
print("\n")
