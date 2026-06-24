#project 1:
# Library book managment system:- 
# ADD/Remove/search books stored in a CSV file using a file handling function for each oreintation try except for file not fopund errors
FILENAME = "books.csv"
# ---------- Add Book ----------
def add_book():
    try:
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        with open(FILENAME, "a") as file:
            file.write(f"{book_id},{title},{author}\n")
        print(" Book added successfully!")
    except Exception as e:
        print(" Error:", e)
# ---------- Remove Book ----------
def remove_book():
    try:
        book_id = input("Enter Book ID to remove: ")
        with open(FILENAME, "r") as file:
            lines = file.readlines()
        found = False
        with open(FILENAME, "w") as file:
            for line in lines:
                if line.strip().startswith(book_id + ","):
                    found = True
                else:
                    file.write(line)
        if found:
            print(" Book removed successfully!")
        else:
            print(" Book not found!")
    except FileNotFoundError:
        print(" File not found! Add books first.")

def search_book():
    try:
        title_search = input("Enter book title to search: ").lower()
        with open(FILENAME, "r") as file:
            found = False
            for line in file:
                book = line.strip().split(",")

                if title_search in book[1].lower():
                    print(" Book Found")
                    print("ID:", book[0])
                    print("Title:", book[1])
                    print("Author:", book[2])
                    found = True

            if not found:
                print(" Book not found!")

    except FileNotFoundError:
        print(" File not found! Add books first.")


def menu():
    while True:
        print("\n Library Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            print(" Exiting program")
            break
        else:
            print(" Invalid choice!")
menu()
print("Thanks for using our system\n use again")
