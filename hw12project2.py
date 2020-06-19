#! /usr/bin/python
# Exercise No.  04
# File Name:    hw12project2.py
# Programmer:   Arthur Utnehmer
# Date: May 6, 2020
#
# Problem Statement: (what you want the code to do)
# Write a program that simulates an automatic teller machine (ATM).
# Since you probably don't have access to a card reader, have the initial
# screen ask for user ID and a PIN. The user ID will be used to look up the
# information for the user's accounts (including the PIN to see whether it matches what the user types).
# Each user will have access to a checking account and a savings account. The user should able to check balances, withdraw cash,
# and transfer money between accounts. Design your interface to be similar to what you see on your local ATM. The user
# account information should be stored in a file when the program terminates. This file is read in again when the program restarts.
#
# Overall Plan (step-by-step,howyou want the code to make it happen):
# 1. Get the number that represents which Fibonacci number to stop at.
# 2. Loop by adding the previouse two to get the next number.


class ATM:
    def __init__(self, filename):
        self.filename = filename
        self.load_customers()
        self.id_pin_dict = {}
        for cust in self.cust_list:
            self.id_pin_dict[cust.getId()] = cust.getPin()
        self.cust = self.enterSystem()
        self.menu()


    def enterSystem(self):
        id = input("Please enter your user id:")
        pin = input("Please Enter the pin connected to the account:")
        while(id, pin) not in self.id_pin_dict.items():
            print("\n Invalid id or pin.")
            id = input("Enter the user id.")
            pin = input("Enter your pin.")
        return [cust for cust in self.cust_list if cust.getId() == id][0]

    def menu(self):
        print("\n Menu \n" + "(1) see balance\n" + "(2) Withdraw\n"+ "(3) Deposit \n" + "(4) Transfer")
        choice = eval(input('select 1-4:'))
        if(choice == 1):
            self.getBalance()
        elif(choice == 2):
            self.withdraw()
        elif(choice == 3):
            self.deposit()
        elif(choice == 4):
            self.transfer()

        self.another()

    def getBalance(self):
        acct = input("\n Checking or Savings (c or s)")
        if acct[0].lower() == 'c':
            print("Checkings balance is :", self.cust.getCheckingBalance())
        else:
            print("Savings balance is :", self.cust.getCheckingBalance())

        self.another()

    def withdraw(self):
        acct = input("\n Checkings or savings (c or s)").lower()
        ammount = eval(input("What is the ammount you would likw to witdraw?"))
        if acct == 'c':
            if 0 <= ammount <= self.cust.getCheckingBalance():
                self.cust.widthdraw(ammount, 'c')
                print("New checking Balance is:" , self.cust.getCheckingBalance())

            elif ammount < 0:
                print("To poor")
            else:
                print("To poor")
        else:
            if 0 <= ammount <= self.cust.getSavingsBalance():
                self.cust.widthdraw(ammount, 's')
                print("New savings Balance is:" , self.cust.getSavingsBalance())

            elif ammount < 0:
                print("To poor")
            else:
                print("To poor")

        self.another()


    def deposit(self):
            acct = input("\n Checking (c) or Savings (s) ").lower()
            ammt = eval(input("Enter the ammount you would like to deposit."))
            if acct == 'c':
                self.cust.deposit(ammt, 'c')
                print("New Balance is:", self.cust.getCheckingBalance())

            else:
                self.cust.deposit(ammt, 's')
                print("New savings Balance:", self.cust.getSavingsBalance())
            self.another()

    def deposit(self, ammount, type):
        acct = type
        ammt = ammount
        if acct == 'c':
            self.cust.deposit(ammt, 'c')
            print("New Balance is:", self.cust.getCheckingBalance())

        else:
            self.cust.deposit(ammt, 's')
            print("New savings Balance:", self.cust.getSavingsBalance())
        self.another()

    def transfer(self):
        type = input("\n Checking to savings (cts) or savings to checkings? (stc)")
        ammount = eval(input("Ammount to transfer:"))
        if(type == "cts"):
            if 0 <= ammount <= self.cust.getCheckingBalance():
                self.cust.widthdraw(ammount, 'c')
                print("New checking Balance:", self.cust.getCheckingBalance())
                self.cust.deposit(ammount, 's')
                print("New Savings Balance:", self.cust.getSavingsBalance())
            else:
                print("To poor.")

        else:
            if(0<= ammount <= self.cust.getSavingsBalance()):
                self.cust.widthdraw(ammount, 's')
                print("New Balance", self.cust.getSavingsBalance())
                self.deposit(ammount, 'c')
                print("new Checking balance", self.cust.getCheckingBalance())
            else:
                print("To poor")


    def another(self):
        response = input("\n Do you have another transaction to make?")
        if response[0].lower() =='y':
            self.menu()
        else:
            self.close()

    def close(self):
        print("exiting")
        self.saveCustomers()
        exit()

    def load_customers(self):
        try:
            file = open(self.filename, 'r')
        except FileNotFoundError:
            file = open(self.filename, 'w')
            file.close()
            file = open(self.filename, 'r')
        self.cust_list = []
        for line in file:
            id, pin, cb, sb = line.split(' ')
            checkings = eval(cb)
            savings = eval(sb)
            self.cust_list.append(Customer(id, pin, checkings, savings))
        file.close()



    def saveCustomers(self):
        file = open(self.filename, 'w')
        output_string = ''
        for cust in self.cust_list:
            print(cust.getSavingsBalance())
            file.write(str(cust.getId()) + ' ')
            file.write(str(cust.getPin()) + ' ')
            file.write(str(cust.getCheckingBalance()))
            file.write(' ')
            file.write(str(cust.getSavingsBalance()))
        file.close()


class Customer:
    def __init__(self, id, pin, checkingBalance, savingBalance):
        self.id = id
        self.pin = pin
        self.checking_balance = checkingBalance
        self.savings_balance = savingBalance

    def getId(self):
        return self.id

    def getPin(self):
        return self.pin

    def getCheckingBalance(self):
        return self.checking_balance

    def getSavingsBalance(self):
        return self.savings_balance

    def widthdraw(self, ammount, account):
        if account == "c":
            self.checking_balance -= ammount
        else:
            self.savings_balance -= ammount

    def deposit(self, ammount, account):
        if account == 'c':
            self.checking_balance += ammount
        else:
            self.savings_balance += ammount

def main():
    fileName = "save.txt"
    atm = ATM(fileName)

main()