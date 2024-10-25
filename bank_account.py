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
        self.balance = balance

