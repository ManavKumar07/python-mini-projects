# project 2:
# Expense tracker:- 
# Log daily expanses to a .txt file, read and summarize by category using function  handle invalid input via expception handling

def add_expense(amount, category):
    try:
        amount = float(amount)
        with open("expenses.txt", "a") as file:
            file.write(f"{category},{amount}\n")
        print("Expense added successfully")

    except ValueError:
        print("Invalid amount entered")


def summary():
    totals = {}
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                category, amount = line.strip().split(",")
                totals[category] = totals.get(category, 0) + float(amount)

        print("\nExpense Summary:")
        for cat, amt in totals.items():
            print(cat, "=", amt)

    except FileNotFoundError:
        print("No expense file found")


# -------- MAIN PROGRAM --------
while True:
    print("\n1. Add Expense")
    print("2. View Summary")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amt = input("Enter amount: ")
        cat = input("Enter category: ")
        add_expense(amt, cat)

    elif choice == "2":
        summary()

    elif choice == "3":
        print("Thank you! Exiting program.")
        break

    else:
        print("Invalid choice! Try again.")
        