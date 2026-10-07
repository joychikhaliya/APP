import csv
import re

# Regex pattern for Account Number validation
# Example format: ACC followed by 6 digits (e.g., ACC123456)
ACCOUNT_PATTERN = r"^ACC\d{6}$"

class Customer:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"Account: {self.account_number}, Name: {self.name}, Balance: ₹{self.balance}"

class Bank:
    def __init__(self, filename):
        self.filename = filename
        self.customers = []
        self.load_customers()

    def load_customers(self):
        """Read customer records from CSV file"""
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    account_number = row['AccountNumber']
                    name = row['Name']
                    balance = row['Balance']
                    # Validate account number format
                    if re.match(ACCOUNT_PATTERN, account_number):
                        self.customers.append(Customer(account_number, name, balance))
                    else:
                        print(f"Invalid account number format: {account_number}")
        except FileNotFoundError:
            print("Error: customers.csv file not found!")

    def display_all(self):
        """Display all customer records"""
        if not self.customers:
            print("No customer records available.")
        else:
            print("\n--- All Customer Records ---")
            for customer in self.customers:
                print(customer)

    def search_by_account(self, account_number):
        """Search customer by account number"""
        if not re.match(ACCOUNT_PATTERN, account_number):
            print("Invalid account number format!")
            return
        for customer in self.customers:
            if customer.account_number == account_number:
                print("\n--- Customer Found ---")
                print(customer)
                return
        print("Customer not found.")

# -------------------------------
# Example Usage
# -------------------------------
if __name__ == "__main__":
    bank = Bank("customers.csv")

    # Display all records
    bank.display_all()

    # Search by account number
    acc_no = input("\nEnter Account Number to search (e.g., ACC123456): ")
    bank.search_by_account(acc_no)




#SAMPLE

AccountNumber,Name,Balance
ACC123456,Rahul Sharma,50000
ACC654321,Neha Patil,75000
ACC111222,Amit Kumar,30000
