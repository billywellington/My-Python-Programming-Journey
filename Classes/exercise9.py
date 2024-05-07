# Exercise 9: Implementing a Bank with Multiple Account Types
# Question:
# Extend the BankAccount class from Exercise 4 to support different types of accounts,
# such as CheckingAccount and SavingsAccount.
# Each account type may have different rules for deposits, withdrawals, and interest calculations.
# Implement the necessary methods and attributes for each account type.

import random
class BankAccount:

    def __init__(self, name, ID, cell, address):
        self.name = name
        self.ID = ID
        self.cell = cell
        self.address = address


class CheckingAccount(BankAccount):
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print(f"Deposit made into {self.name}'s account with account number {self.name}. Balance is ZAR {self.balance}")

    def withdraw(self, amount):
        self.amount = amount
        #error handling to ensure that withdrawals cannot result in a negative balance.
        if self.amount > self.balance:
            print("Sorry! You have insufficient funds...You cannot withdraw amount more than available balance")

        else:
            self.balance = self.balance - self.amount
            print(f"Withdrawal made from {self.name}'s account with account number {self.name}. Balance is ZAR {self.balance}")

class SavingsAccount(BankAccount):

    def open_sav_acc(self, name, ID, cell, address):
        self.name = name
        self.ID = ID
        self.cell = cell
        self.address = address

        acc_num = random.randint(1000000000, 3000000000)

        print("Please check the following if has been captured correctly.\n")
        print(f"{self.name}\n{self.ID}\n{self.cell}\n{self.address}")
        correction_choice = input("Is there anything you'd like correct?\nPress 0 if everything is OK\n 1 to change/correct your name,\n 2 to change/correct your ID, \n3 to change/correct your cell,\n 4 to change/correct your address\n")

        while correction_choice != "1" or "2" or "3" or "4":
            correction_choice = input("Incorrect input.\nPress 0 if everything is OK\n 1 to change/correct your name,\n 2 to change/correct your ID, \n3 to change/correct your cell,\n 4 to change/correct your address\n")
        if correction_choice == "1":
            self.name = input("Enter your correct name: ")
        elif correction_choice == "2":
            self.ID = input("Enter your correct ID: ")
        elif correction_choice == "3":
            self.cell = input("Enter your correct cell: ")
        elif correction_choice == "4":
            self.address = input("Enter your correct address: ")
        else:
            print(f"Congrats! You've successfully opened your Evergreen Bank Checking Account. Here's your account number: {acc_num}")

        print("Please make a deposit of R100 to activate your account")
        #create terms and conditions and fees structure
        print("Please take note of the following fees:\n-------------------------------\nEVERGREEN BANK SAVINGS ACCOUNT FEES\n-------------------------------\nDeposit: R5\nWithdrawal: R10\n")
        print("Presented herein are the prevailing interest rates, indicative of the potential growth of your savings over a specified duration.")
        print("Please choose the growth options you'd like to go with:\n1. 1 Year - Growth Rate 5%\n2. 2 Year - Growth Rate 12%\n3. 3 Year - Growth Rate 20%\n4. 5 Year - Growth Rate 55%\n5. 10 Year - Growth Rate 5%\n")
            

    # def open_check_acc(self, name, ID, cell, address):
    #     self.name = name
    #     self.ID = ID
    #     self.cell = cell
    #     self.address = address

    # Method named deposit() to add funds to the account.
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print(  f"Deposit made into {self.name}'s account with account number {self.account_number}. Balance is ZAR {self.balance}")

    # Method named withdraw() to subtract funds from the account,
    def withdraw(self, amount):
        self.amount = amount
        # error handling to ensure that withdrawals cannot result in a negative balance.
        if self.amount > self.balance:
            print("Sorry! You have insufficient funds...You cannot withdraw amount more than available balance")

        else:
            self.balance = self.balance - self.amount
            print(
                f"Withdrawal made from {self.account_holder}'s account with account number {self.account_number}. Balance is ZAR {self.balance}")


user_choice = input("Hello Welcome to Evergreen Bank. \nPlease choose which account you'd like to open today:\n1.Checking Account\n2.Savings Account.\nSelect \"1\" or \"2\": ")

#making sure the user enters 1 or 2
while user_choice != "1" or "2":
    user_choice = input("Please enter either 1 or 2\n1.Checking Account\n2.Savings Account.\nSelect your choice: ")
if user_choice == "1":
    #open checking account
else:
    #open savings account
