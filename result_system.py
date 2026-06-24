import grade_module

student1 = (1, "sachin")
student2 = (2, "Akhil")

students = [student1, student2]

marks = {
    1: 85,
    2: 92
}

file = open("results.txt", "w")
results = []

for student in students:
    roll, name = student
    total = marks[roll]

    grade = grade_module.calculate_grade(total)

    results.append((roll, name, total, grade))
    file.write(f"{roll} {name} {total} {grade}\n")

file.close()

results.sort(key=lambda x: x[2], reverse=True)

print("---- RANK LIST ----")
rank = 1
for r in results:
    print(f"Rank {rank}: {r[1]} - Marks: {r[2]} - Grade: {r[3]}")
    rank += 1
