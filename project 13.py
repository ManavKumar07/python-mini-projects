# AUTOMATED DATA COLLECTOR (SCRAPE DATA & SAVE IT TO CSV)
import csv
import os

FILE_NAME = "data.csv"

# Create CSV file if not exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Age", "City", "Email"])


# Add Record
def add_record():
    print("\n------ Add New Record ------")

    id = input("Enter ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    city = input("Enter City: ")
    email = input("Enter Email: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([id, name, age, city, email])

    print("\nRecord Saved Successfully!\n")


# View Records
def view_records():
    print("\n------ All Records ------\n")

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            print("{:<8} {:<20} {:<8} {:<15} {}".format(*row))


# Search Record
def search_record():
    search = input("\nEnter Name to Search: ").lower()

    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        next(reader)

        for row in reader:
            if row[1].lower() == search:
                print("\nRecord Found")
                print("-----------------------------")
                print("ID    :", row[0])
                print("Name  :", row[1])
                print("Age   :", row[2])
                print("City  :", row[3])
                print("Email :", row[4])
                found = True

    if not found:
        print("\nRecord Not Found.")


# Count Records
def total_records():
    with open(FILE_NAME, "r") as file:
        reader = list(csv.reader(file))

    print("\nTotal Records =", len(reader) - 1)


# Delete Record
def delete_record():
    delete_name = input("\nEnter Name to Delete: ").lower()

    rows = []

    deleted = False

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        header = next(reader)
        rows.append(header)

        for row in reader:
            if row[1].lower() != delete_name:
                rows.append(row)
            else:
                deleted = True

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    if deleted:
        print("\nRecord Deleted Successfully.")
    else:
        print("\nRecord Not Found.")


# Main Menu
while True:

    print("\n==============================")
    print(" AUTOMATED DATA COLLECTOR")
    print("==============================")
    print("1. Add Record")
    print("2. View Records")
    print("3. Search Record")
    print("4. Total Records")
    print("5. Delete Record")
    print("6. Exit")

    choice = input("\nEnter Your Choice: ")

    if choice == "1":
        add_record()

    elif choice == "2":
        view_records()

    elif choice == "3":
        search_record()

    elif choice == "4":
        total_records()

    elif choice == "5":
        delete_record()

    elif choice == "6":
        print("\nThank You!")
        break

    else:
        print("\nInvalid Choice!")