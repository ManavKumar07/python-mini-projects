#Hospital management 
# HOSPITAL MANAGEMENT SYSTEM:-
# 1. Patient records are stored in dictionaries.
# 2. List maintain patient ID.
# 3. Create classes for patients and doctors.
# 4. Functions scheduled appointments.
# 5. Store records in file.
# 6. Handle invalid patient information through exception.
# Patient IDs stored in list

patient_ids = [1, 2]


patients = {
    1: {"name": "Rahul", "age": 25, "disease": "Fever"},
    2: {"name": "Anita", "age": 30, "disease": "Cold"}
}

# File function to store records
def store_record(message):
    f = open("hospital_records.txt", "a")
    f.write(message + "\n")
    f.close()


# Patient class
class Patient:
    def __init__(self, pid, name, age, disease):
        self.pid = pid
        self.name = name
        self.age = age
        self.disease = disease

    def show_details(self):
        try:
            if self.age <= 0:
                raise ValueError("Invalid Patient Age")

            print("Patient ID:", self.pid)
            print("Name:", self.name)
            print("Age:", self.age)
            print("Disease:", self.disease)

            store_record(f"Patient {self.pid} {self.name} {self.age} {self.disease}")

        except ValueError as e:
            print("Error:", e)


# Doctor class
class Doctor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization


# Appointment function
def schedule_appointment(patient, doctor):
    print(f"Appointment Scheduled with Dr. {doctor.name}")
    store_record(f"Appointment: Patient {patient.name} with Dr. {doctor.name}")


# ---------------- MAIN PROGRAM ----------------
print("---- HOSPITAL MANAGEMENT SYSTEM ----")

doctor1 = Doctor("Sharma", "General Physician")

for pid in patient_ids:
    data = patients[pid]
    patient = Patient(pid, data["name"], data["age"], data["disease"])

    print("\nPatient Details:")
    patient.show_details()
    schedule_appointment(patient, doctor1)


# ---------------- EXAM RESULT SYSTEM ----------------

# Student details stored in tuples
student1 = (1, "Rahul")
student2 = (2, "Anita")
student3 = (3, "Aman")

# Student records stored in list
students = [student1, student2, student3]

# Marks stored in dictionary
marks = {
    1: 85,
    2: 92,
    3: 78
}

# Grade calculation function
def calculate_grade(total):
    if total >= 90:
        return "A"
    elif total >= 75:
        return "B"
    elif total >= 60:
        return "C"
    else:
        return "D"


# File to save results
file = open("results.txt", "w")

results = []

# Process results
for student in students:
    roll, name = student
    total = marks[roll]
    grade = calculate_grade(total)

    results.append((roll, name, total, grade))
    file.write(f"{roll} {name} {total} {grade}\n")

file.close()

# Generate rank list
results.sort(key=lambda x: x[2], reverse=True)

print("---- RANK LIST ----")
rank = 1
for r in results:
    print("Rank", rank, ":", r[1], "- Marks:", r[2], "- Grade:", r[3])
    rank += 1