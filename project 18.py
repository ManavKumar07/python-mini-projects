# BANK ACCOUNT SYTEM
import json
import os


class BankAccount:

    FILE = "accounts.json"

    def __init__(self):
        if not os.path.exists(self.FILE):
            with open(self.FILE, "w") as file:
                json.dump([], file)

    # ---------------- File Functions ----------------

    def load_data(self):
        with open(self.FILE, "r") as file:
            return json.load(file)

    def save_data(self, data):
        with open(self.FILE, "w") as file:
            json.dump(data, file, indent=4)

    # ---------------- Create Account ----------------

    def create_account(self):

        data = self.load_data()

        try:
            acc_no = int(input("Enter Account Number : "))

            for acc in data:
                if acc["Account Number"] == acc_no:
                    print("Account Already Exists.")
                    return

            name = input("Enter Name : ")
            pin = input("Create 4-digit PIN : ")
            balance = float(input("Enter Initial Balance : "))

            account = {
                "Account Number": acc_no,
                "Name": name,
                "PIN": pin,
                "Balance": balance,
                "Transactions": [f"Account Opened with ₹{balance}"]
            }

            data.append(account)
            self.save_data(data)

            print("\nAccount Created Successfully.\n")

        except ValueError:
            print("Invalid Input!")

    # ---------------- Login ----------------

    def login(self):

        data = self.load_data()

        try:
            acc_no = int(input("Enter Account Number : "))
            pin = input("Enter PIN : ")

            for acc in data:
                if acc["Account Number"] == acc_no and acc["PIN"] == pin:
                    print(f"\nWelcome {acc['Name']}")
                    self.account_menu(acc)
                    self.save_data(data)
                    return

            print("Invalid Account Number or PIN.")

        except ValueError:
            print("Invalid Input!")

    # ---------------- Account Menu ----------------

    def account_menu(self, account):

        while True:

            print("\n------ ACCOUNT MENU ------")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Transaction History")
            print("5. Logout")

            choice = input("Enter Choice : ")

            if choice == "1":
                self.deposit(account)

            elif choice == "2":
                self.withdraw(account)

            elif choice == "3":
                self.check_balance(account)

            elif choice == "4":
                self.show_history(account)

            elif choice == "5":
                print("Logged Out Successfully.")
                break

            else:
                print("Invalid Choice.")

    # ---------------- Deposit ----------------

    def deposit(self, account):

        try:
            amount = float(input("Enter Amount : "))

            if amount <= 0:
                print("Amount must be positive.")
                return

            account["Balance"] += amount
            account["Transactions"].append(f"Deposited ₹{amount}")

            print("Deposit Successful.")

        except ValueError:
            print("Invalid Amount.")

    # ---------------- Withdraw ----------------

    def withdraw(self, account):

        try:
            amount = float(input("Enter Amount : "))

            if amount <= 0:
                print("Invalid Amount.")
                return

            if amount > account["Balance"]:
                print("Insufficient Balance.")
                return

            account["Balance"] -= amount
            account["Transactions"].append(f"Withdrawn ₹{amount}")

            print("Withdrawal Successful.")

        except ValueError:
            print("Invalid Amount.")

    # ---------------- Balance ----------------

    def check_balance(self, account):

        print(f"\nCurrent Balance : ₹{account['Balance']}")

    # ---------------- History ----------------

    def show_history(self, account):

        print("\n------ Transactions ------")

        for item in account["Transactions"]:
            print(item)


# ---------------- Main Program ----------------

bank = BankAccount()

while True:

    print("\n====== BANK ACCOUNT SYSTEM ======")

    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        bank.create_account()

    elif choice == "2":
        bank.login()

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")