# Exercise 4: Building a Bank Account Class
# Question:
# Define a Python class named BankAccount to represent a simple bank account. The BankAccount class should have:
#
# Attributes for account_number, account_holder, and balance.
# Methods named deposit() and withdraw() to add and subtract funds from the account, respectively.
# Implement error handling to ensure that withdrawals cannot result in a negative balance.

class BankAccount:

    def __init__(self, account_holder, account_number, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    # Method named deposit() to add funds to the account.
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print(f"Deposit made into {self.account_holder}'s account with account number {self.account_number}. Balance is ZAR {self.balance}")

    # Method named withdraw() to subtract funds from the account,
    def withdraw(self, amount):
        self.amount = amount
        #error handling to ensure that withdrawals cannot result in a negative balance.
        if self.amount > self.balance:
            print("Sorry! You have insufficient funds...You cannot withdraw amount more than available balance")

        else:
            self.balance = self.balance - self.amount
            print(f"Withdrawal made from {self.account_holder}'s account with account number {self.account_number}. Balance is ZAR {self.balance}")

bank_account1 = BankAccount("Emma Thompson", 1234567890, 5432)


bank_account1.deposit(1000)
bank_account1.withdraw(100)
bank_account1.withdraw(7000)