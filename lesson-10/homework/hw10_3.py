'''Homework 3. Simple Banking System

Define Account Class:
Create an Account class with attributes like account number, account holder name, and balance.
Define Bank Class:
Create a Bank class that manages a list of accounts.
Include methods to add an account, check balance, deposit money, and withdraw money.
Create Main Program:
Develop a CLI to interact with the Banking system.
Include options to add accounts, check balance, deposit money, and withdraw money.
Enhance Banking System:
Add functionality to transfer money between accounts, display account details, and handle account overdrafts.
Test the Application:
Create instances of accounts and test the functionality of your Banking system.'''
class Account:
    def __init__(self, account_number, holder_name, balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited {amount}. New balance: {self.balance}"
        return "Invalid deposit amount."
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew {amount}. New balance: {self.balance}"
        return "Insufficient funds or invalid amount."
    
    def transfer(self, amount, recipient):
        if 0 < amount <= self.balance:
            self.balance -= amount
            recipient.balance += amount
            return f"Transferred {amount} to {recipient.holder_name}. New balance: {self.balance}"
        return "Insufficient funds or invalid amount."
    
    def __str__(self):
        return f"Account: {self.account_number}, Holder: {self.holder_name}, Balance: {self.balance}"

class Bank:
    def __init__(self):
        self.accounts = {}
    
    def add_account(self, account):
        self.accounts[account.account_number] = account
        return "Account added successfully!"
    
    def get_account(self, account_number):
        return self.accounts.get(account_number, None)
    
    def check_balance(self, account_number):
        account = self.get_account(account_number)
        return account.balance if account else "Account not found."
    
    def deposit_money(self, account_number, amount):
        account = self.get_account(account_number)
        return account.deposit(amount) if account else "Account not found."
    
    def withdraw_money(self, account_number, amount):
        account = self.get_account(account_number)
        return account.withdraw(amount) if account else "Account not found."
    
    def transfer_money(self, sender_acc, receiver_acc, amount):
        sender = self.get_account(sender_acc)
        receiver = self.get_account(receiver_acc)
        if sender and receiver:
            return sender.transfer(amount, receiver)
        return "One or both accounts not found."

def main():
    bank = Bank()
    
    while True:
        print("\nSimple Banking System")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. Display Account Details")
        print("7. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            acc_number = input("Enter account number: ")
            holder_name = input("Enter account holder name: ")
            initial_balance = float(input("Enter initial balance: "))
            account = Account(acc_number, holder_name, initial_balance)
            print(bank.add_account(account))
        
        elif choice == "2":
            acc_number = input("Enter account number: ")
            print(f"Balance: {bank.check_balance(acc_number)}")
        
        elif choice == "3":
            acc_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            print(bank.deposit_money(acc_number, amount))
        
        elif choice == "4":
            acc_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            print(bank.withdraw_money(acc_number, amount))
        
        elif choice == "5":
            sender_acc = input("Enter sender account number: ")
            receiver_acc = input("Enter receiver account number: ")
            amount = float(input("Enter transfer amount: "))
            print(bank.transfer_money(sender_acc, receiver_acc, amount))
        
        elif choice == "6":
            acc_number = input("Enter account number: ")
            account = bank.get_account(acc_number)
            print(account if account else "Account not found.")
        
        elif choice == "7":
            print("Exiting the application.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

    