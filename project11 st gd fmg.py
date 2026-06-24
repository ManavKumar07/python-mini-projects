# project3:
# Student Grade File Manager-
# Read student data from CSV, computes grades using functions, writes updated results back to a new CSV File
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "F"
def add_students():
    try:
        n = int(input("Enter number of students: "))
        with open("students.csv", "w") as file:
            for i in range(n):
                name = input("Enter student name: ")
                marks = int(input("Enter marks: "))
                file.write(name + "," + str(marks) + "\n")
        print("Student data saved successfully")
    except ValueError:
        print("Invalid input! Please enter numbers for marks and count.")
def process_students():
    try:
        with open("students.csv", "r") as infile, open("results.csv", "w") as outfile:
            outfile.write("Name,Marks,Grade\n")
            for line in infile:
                name, marks = line.strip().split(",")
                marks = int(marks)
                grade = calculate_grade(marks)
                outfile.write(name + "," + str(marks) + "," + grade + "\n")
        print("Results file created successfully")
    except FileNotFoundError:
        print("students.csv file not found")
    except ValueError:
        print("Invalid marks found in file")
# -------- MAIN PROGRAM --------
add_students()
process_students()  





