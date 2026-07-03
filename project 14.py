# IPL/SALES DATASET ANALYZER
import pandas as pd
import os

FILE_NAME = "sales.csv"

# Create sample dataset if file doesn't exist
if not os.path.exists(FILE_NAME):
    data = {
        "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer",
                    "Laptop", "Mouse", "Monitor", "Keyboard", "Printer"],
        "Category": ["Electronics", "Accessories", "Accessories", "Electronics",
                     "Electronics", "Electronics", "Accessories",
                     "Electronics", "Accessories", "Electronics"],
        "Quantity": [5, 20, 15, 8, 3, 4, 18, 6, 10, 2],
        "Price": [50000, 500, 1200, 10000, 8000,
                  52000, 550, 9500, 1100, 8500]
    }

    df = pd.DataFrame(data)
    df.to_csv(FILE_NAME, index=False)

# Load Dataset
df = pd.read_csv(FILE_NAME)

while True:
    print("\n========= SALES DATASET ANALYZER =========")
    print("1. View Dataset")
    print("2. First 5 Records")
    print("3. Last 5 Records")
    print("4. Total Sales")
    print("5. Highest Price Product")
    print("6. Lowest Price Product")
    print("7. Average Price")
    print("8. Category-wise Sales")
    print("9. Product-wise Quantity")
    print("10. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        print("\nDataset")
        print(df)

    elif choice == "2":
        print(df.head())

    elif choice == "3":
        print(df.tail())

    elif choice == "4":
        df["Total"] = df["Quantity"] * df["Price"]
        print("\nTotal Sales = ₹", df["Total"].sum())

    elif choice == "5":
        print("\nHighest Price Product")
        print(df.loc[df["Price"].idxmax()])

    elif choice == "6":
        print("\nLowest Price Product")
        print(df.loc[df["Price"].idxmin()])

    elif choice == "7":
        print("\nAverage Price =", round(df["Price"].mean(), 2))

    elif choice == "8":
        df["Total"] = df["Quantity"] * df["Price"]
        print("\nCategory-wise Sales")
        print(df.groupby("Category")["Total"].sum())

    elif choice == "9":
        print("\nProduct-wise Quantity")
        print(df.groupby("Product")["Quantity"].sum())

    elif choice == "10":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")