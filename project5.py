#PROJECT 5
#Student result managment system- store student names and marks in a dictionary. use sets to detect duplicate number
students = {}
roll_set = set()

n = int(input("Enter number of students: "))

for i in range(n):
    roll = int(input("Enter roll number: "))
    
    if roll in roll_set:
        print("Duplicate roll number found!")
        continue
    
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    
    students[roll] = (name, marks)
    roll_set.add(roll)

print("\nStudent Records:")
for roll, data in students.items():
    print(roll, data)
