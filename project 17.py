#GRADE MANAGMENT SYSTEM WITH FILE STORAGE
import json
import os


class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / len(self.marks)

    def grade(self):
        p = self.percentage()

        if p >= 90:
            return "A+"
        elif p >= 80:
            return "A"
        elif p >= 70:
            return "B"
        elif p >= 60:
            return "C"
        elif p >= 50:
            return "D"
        else:
            return "Fail"

    def to_dict(self):
        return {
            "Roll": self.roll,
            "Name": self.name,
            "Marks": self.marks,
            "Total": self.total(),
            "Percentage": round(self.percentage(), 2),
            "Grade": self.grade()
        }


class GradeManagementSystem:

    FILE = "students.json"

    def __init__(self):
        if not os.path.exists(self.FILE):
            with open(self.FILE, "w") as f:
                json.dump([], f)

    def load(self):
        with open(self.FILE, "r") as f:
            return json.load(f)

    def save(self, data):
        with open(self.FILE, "w") as f:
            json.dump(data, f, indent=4)

    def add_student(self):

        try:
            roll = int(input("Enter Roll Number : "))
            name = input("Enter Name : ")

            marks = []

            print("Enter marks of 5 subjects")

            for i in range(5):
                m = float(input(f"Subject {i+1}: "))
                marks.append(m)

            student = Student(roll, name, marks)

            data = self.load()
            data.append(student.to_dict())
            self.save(data)

            print("\nStudent Added Successfully.\n")

        except ValueError:
            print("Invalid Input!")

    def display(self):

        data = self.load()

        if not data:
            print("No Records Found.")
            return

        print("\n----- STUDENT RECORDS -----\n")

        for s in data:
            print("Roll :", s["Roll"])
            print("Name :", s["Name"])
            print("Marks :", s["Marks"])
            print("Total :", s["Total"])
            print("Percentage :", s["Percentage"])
            print("Grade :", s["Grade"])
            print("-" * 40)

    def search(self):

        roll = int(input("Enter Roll Number : "))

        data = self.load()

        for s in data:
            if s["Roll"] == roll:
                print("\nStudent Found")
                print(s)
                return

        print("Student Not Found.")

    def delete(self):

        roll = int(input("Enter Roll Number : "))

        data = self.load()

        new_data = [s for s in data if s["Roll"] != roll]

        if len(data) == len(new_data):
            print("Student Not Found.")
        else:
            self.save(new_data)
            print("Record Deleted Successfully.")


def menu():

    gms = GradeManagementSystem()

    while True:

        print("\n===== GRADE MANAGEMENT SYSTEM =====")

        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter Choice : ")

        if choice == "1":
            gms.add_student()

        elif choice == "2":
            gms.display()

        elif choice == "3":
            gms.search()

        elif choice == "4":
            gms.delete()

        elif choice == "5":
            print("Thank You")
            break

        else:
            print("Invalid Choice")


menu()