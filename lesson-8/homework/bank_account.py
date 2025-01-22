import os
import json

class Account:
    def __init__(self, account_number, name, balance):
        self.account_number=account_number
        self.name=name 
        self.balance=balance
    def to_dict(self):
        return{
            'account_number':self.account_number,
            'name': self.name,
            'balance':self.balance
        }
    @staticmethod
    def from_dict(data):
        return Account(data["account_number"],data["name"],data["balance"])

class Bank:
    def __init__(self):
        self.accounts={}
        self.load_from_file()

    def create_account(self,name,initial_deposit):
        account_number=len(self.accounts)+1
        new_account=Account(account_number,name, initial_deposit)
        self.accounts[account_number]=new_account
        self.save_to_file()
        print(f"Account was created! and the number account is {account_number}")
    def view_account(self,account_number):
        account=self.accounts.get(account_number)
        if account:
            print(f"The account number : {account.account_number}")
            print(f"The name: {account.name}")
            print(f"Balance: {account.balance}")
        else:
            print("Can`t found that account number")
    def deposit(self,account_number, amount):
        account=self.accounts.get(account_number)
        if account and amount>0:
            account.balance+=amount
            print(f"{amount} was added to account. New balance is {account.balance}")
        else:
            print("Incorrect amount or undefined account number")
    def withdraw(self,account_number, amount):
        account=self.accounts.get(account_number)
        if account and 0<amount<=account.balance:
            account.balance-=amount
            print(f"{amount} was withdrawn from account. New balance is {account.balance}")
        else:
            print("Incorrect amount or undefined account number")
    def save_to_file(self):
        with open("accounts.txt", "w") as file:
            data=[account.to_dict() for account in self.accounts.values()]
            json.dump(data,file)

    def load_from_file(self):
        if os.path.exists("accounts.txt"):
            with open("accounts.txt","r") as file:
                data=json.load(file)
                for acc_data in data:
                    account=Account.from_dict(acc_data)
                    self.accounts[account.account_number]=account

def main():
    bank=Bank()
    while True:
        print("\n Menu:")
        print("1. Create an account")
        print("2. View the account")
        print("3. Deposit to account")
        print("4. Withdraw from account")
        print("5. Exit")
        choice=input("choose (1-5): ")
        if choice=='1':
            name=input("Enter your name: ")
            initial_deposit=float(input("enter the initial_deposit"))
            bank.create_account(name,initial_deposit)
        elif choice=='2':
            account_number=int(input("Enter the number of your account: "))
            bank.view_account(account_number)
        elif choice=='3':
            account_number=int(input("Enter the number of your account: "))
            amount=float(input("enter the amount which should be added"))
            bank.deposit(account_number, amount)
        elif choice=='4':
            account_number=int(input("Enter the number of your account: "))
            amount=float(input("Enter the amount which must be withdrawn: "))
            bank.withdraw(account_number,amount)
        elif choice=='5':
            bank.save_to_file()
            print("All accounts were saved. Exiting...")
            break
        else:
            print("Incorrect choice")

if __name__=="__main__":
    main()
