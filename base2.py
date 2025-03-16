import time
import calendar 
from datetime import datetime

class Transaction:
    def __init__(self, date, amount, description, type_transaction):
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # current date and time of the transaction
        self.amount = amount
        self.description = description
        self.type_transaction = type_transaction
        
    def __str__(self):
        return f"{self.date} - {self.description}: {self.type_transaction} ${self.amount:.2f}"

class InventoryItem:
    def __init__(self, name, quantity, unit_price):
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price
        
    def __str__(self):
        return f"Item: {self.name}, Quantity: {self.quantity}, Unit Price: ${self.unit_price:.2f}, Total Value: ${self.quantity * self.unit_price:.2f}"

class Account:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        
    def credit(self, amount):
        self.balance += amount
        
    def debit(self, amount):
        self.balance -= amount
        
    def __str__(self):
        return f"Account: {self.name}, Balance: ${self.balance:.2f}"

class AccountingSystem:
    def __init__(self):
        self.report = []
        self.transactions = [] 
        self.inventory = {}
        self.accounts = {}
        
    def adding_accounts(self, name):
        if name not in self.accounts:
            self.accounts[name] = Account(name)
            print(f"Account '{name}' created")
        else:
            print(f"Account '{name}' was already created")
            
    def adding_transactions(self, account_name, amount, type_transaction):
        account = self.accounts.get(account_name)
        if account:
            if type_transaction == "credit":
                account.credit(amount)
            elif type_transaction == "debit":
                account.debit(amount)
            self.transactions.append(Transaction(datetime.now(), amount, f"{type_transaction} for {account_name}", type_transaction))
            print(f"Transaction added")
        else:
            print(f"Account '{account_name}' does not exist")
    
    def add_inventory_item(self, name, quantity, unit_price):
        if name in self.inventory:
            self.inventory[name].quantity += quantity
            print(f"Updated quantity for '{name}' in inventory")
        else:
            self.inventory[name] = InventoryItem(name, quantity, unit_price)
            print(f"Added '{name}' to inventory")
    
    def remove_inventory_item(self, name, quantity):
        if name in self.inventory:
            if self.inventory[name].quantity >= quantity:
                self.inventory[name].quantity -= quantity
                print(f"Removed {quantity} of '{name}' from inventory")
                if self.inventory[name].quantity == 0:
                    del self.inventory[name]
                    print(f"'{name}' is now out of stock and has been removed from inventory")
            else:
                print(f"Error: Not enough '{name}' in inventory. Current quantity: {self.inventory[name].quantity}")
        else:
            print(f"Error: '{name}' not found in inventory")
    
    def update_inventory_price(self, name, new_price):
        if name in self.inventory:
            self.inventory[name].unit_price = new_price
            print(f"Updated price for '{name}' to ${new_price:.2f}")
        else:
            print(f"Error: '{name}' not found in inventory")
    
    def check_inventory(self):
        print("\nCurrent Inventory:")
        if not self.inventory:
            print("Inventory is empty")
        else:
            total_value = 0
            for item in self.inventory.values():
                print(item)
                total_value += item.quantity * item.unit_price
            print(f"\nTotal Inventory Value: ${total_value:.2f}")
          
    def generate_report(self):
        print("\nYour Accounting Report:") 
        if not self.transactions:
            print("Sorry, there is no transaction records")
        else:
            sorted_transactions = sorted(self.transactions, key=lambda x: x.date)
            for transaction in sorted_transactions:
                print(transaction)
        for account in self.accounts.values():
            print(account)

def display_menu():
    print("\nWELCOME TO YOUR ACCOUNTING SYSTEM MENU!")
    print("1. Add an account")
    print("2. Add a transaction")
    print("3. Inventory Management")
    print("4. Generate your report")
    print("5. Check your balance")
    print("6. Exit")
    
def display_inventory_menu():
    print("\nInventory Management Menu:")
    print("1. Add item to inventory")
    print("2. Remove item from inventory")
    print("3. Update item price")
    print("4. Check inventory")
    print("5. Return to main menu")

def main():
    accounting_system = AccountingSystem()
    
    while True:
        display_menu()
        choice = input("Please enter an option (1-6): ")
        
        if choice == '1':
            name = input("Please enter the name of the new account: ")
            accounting_system.adding_accounts(name)
        elif choice == '2':
            account_name = input("Please enter the account name: ")
            amount = float(input("Please enter the amount: $"))    
            type_transaction = input("Please enter the transaction type [debit / credit]: ")
            
            if type_transaction.lower() not in ['credit', 'debit']:
                print("Invalid transaction type, please enter debit or credit.")
                continue
            accounting_system.adding_transactions(account_name, amount, type_transaction.lower())
        elif choice == '3':
            while True:
                display_inventory_menu()
                inventory_choice = input("Please enter an option (1-5): ")
                
                if inventory_choice == '1':
                    name = input("Enter item name: ")
                    quantity = int(input("Enter quantity: "))
                    unit_price = float(input("Enter unit price: $"))
                    accounting_system.add_inventory_item(name, quantity, unit_price)
                elif inventory_choice == '2':
                    name = input("Enter item name: ")
                    quantity = int(input("Enter quantity to remove: "))
                    accounting_system.remove_inventory_item(name, quantity)
                elif inventory_choice == '3':
                    name = input("Enter item name: ")
                    new_price = float(input("Enter new unit price: $"))
                    accounting_system.update_inventory_price(name, new_price)
                elif inventory_choice == '4':
                    accounting_system.check_inventory()
                elif inventory_choice == '5':
                    break
                else:
                    print("Invalid option. Please try again.")
        elif choice == '4':
            accounting_system.generate_report()
        elif choice == '5':
            print("\nAccount Balances:")
            for account in accounting_system.accounts.values():
                print(account)
        elif choice == '6':
            print("Thank you for using the Accounting System. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
