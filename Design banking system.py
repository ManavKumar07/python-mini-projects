# ---------- Account numbers stored in file ----------
file = open("accounts.txt", "w")
file.write("1001\n1002\n")
file.close()

# ---------- Customer details stored in dictionary ----------
accounts = {
    1001: {"name": "Amit", "balance": 5000},
    1002: {"name": "Neha", "balance": 8000}
}

# ---------- Store transaction in file ----------
def store_transaction(msg):
    f = open("transactions.txt", "a")
    f.write(msg + "\n")
    f.close()


# ---------- BankAccount class ----------
class BankAccount:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
        store_transaction(f"{self.acc_no} Deposited {amount}")

    def withdraw(self, amount):
        try:
            if amount > self.balance:
                raise ValueError("Insufficient Balance")

            self.balance -= amount
            print("Withdrawn:", amount)
            store_transaction(f"{self.acc_no} Withdrawn {amount}")

        except ValueError as e:
            print("Error:", e)

    def balance_enquiry(self):
        print("Balance:", self.balance)
        store_transaction(f"{self.acc_no} Balance {self.balance}")


# ---------- MAIN PROGRAM ----------
print("---- BANKING SYSTEM ----")

acc_no = int(input("Enter Account Number: "))

if acc_no in accounts:
    data = accounts[acc_no]
    user = BankAccount(acc_no, data["name"], data["balance"])

    print("Welcome,", user.name)

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Balance Enquiry")
        print("4. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            amt = int(input("Enter amount to deposit: "))
            user.deposit(amt)

        elif choice == 2:
            amt = int(input("Enter amount to withdraw: "))
            user.withdraw(amt)

        elif choice == 3:
            user.balance_enquiry()

        elif choice == 4:
            print("Thank you!")
            break

        else:
            print("Invalid choice")

else:
    print("Invalid Account Number")