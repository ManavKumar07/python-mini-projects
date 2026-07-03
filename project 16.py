#STUDENT MARKS ANALYZER WITH PANDAS
import pandas as pd
import os

FILE_NAME = "students.csv"

# Create CSV file if it doesn't exist
if not os.path.exists(FILE_NAME):
    df = pd.DataFrame(columns=[
        "Roll No", "Name", "Math", "Science", "English",
        "Total", "Percentage", "Grade"
    ])
    df.to_csv(FILE_NAME, index=False)


# Grade Function
def get_grade(per):
    if per >= 90:
        return "A+"
    elif per >= 80:
        return "A"
    elif per >= 70:
        return "B"
    elif per >= 60:
        return "C"
    elif per >= 50:
        return "D"
    else:
        return "Fail"
    
# Add Student
def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")

    math = int(input("Math Marks: "))
    science = int(input("Science Marks: "))
    english = int(input("English Marks: "))

    total = math + science + english
    percentage = round(total / 3, 2)
    grade = get_grade(percentage)

    new_data = pd.DataFrame({
        "Roll No": [roll],
        "Name": [name],
        "Math": [math],
        "Science": [science],
        "English": [english],
        "Total": [total],
        "Percentage": [percentage],
        "Grade": [grade]
    })

    df = pd.read_csv(FILE_NAME)
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(FILE_NAME, index=False)

    print("\nStudent Record Saved Successfully.")

# View Students
def view_students():
    df = pd.read_csv(FILE_NAME)

    if df.empty:
        print("\nNo Records Found.")
    else:
        print("\nStudent Records\n")
        print(df.to_string(index=False))

# Search Student
def search_student():
    name = input("\nEnter Student Name: ")

    df = pd.read_csv(FILE_NAME)

    result = df[df["Name"].str.lower() == name.lower()]

    if result.empty:
        print("\nStudent Not Found.")
    else:
        print("\nRecord Found\n")
        print(result.to_string(index=False))

# Show Topper
def topper():
    df = pd.read_csv(FILE_NAME)

    if df.empty:
        print("\nNo Student Records.")
        return

    top = df.loc[df["Total"].idxmax()]

    print("\n******** TOPPER ********")
    print("Roll No    :", top["Roll No"])
    print("Name       :", top["Name"])
    print("Total      :", top["Total"])
    print("Percentage :", top["Percentage"])
    print("Grade      :", top["Grade"])


# Total Students
def total_students():
    df = pd.read_csv(FILE_NAME)
    print("\nTotal Students:", len(df))

# Class Average
def class_average():
    df = pd.read_csv(FILE_NAME)

    if df.empty:
        print("\nNo Records Found.")
    else:
        print("\nAverage Percentage:", round(df["Percentage"].mean(), 2))


# Main Program
while True:

    print("\n===================================")
    print("   STUDENT MARKS ANALYZER (PANDAS)")
    print("===================================")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Show Topper")
    print("5. Total Students")
    print("6. Class Average")
    print("7. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        topper()

    elif choice == "5":
        total_students()

    elif choice == "6":
        class_average()

    elif choice == "7":
        print("\nThank You!")
        break

    else:
        print("\nInvalid Choice.")