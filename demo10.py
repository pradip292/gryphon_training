students = [
    {"name": "Alice", "age": 20, "grade": 85.5},
    {"name": "Bob", "age": 19, "grade": 92.3},
    {"name": "Charlie", "age": 21, "grade": 89.1},
    {"name": "David", "age": 18, "grade": 95.7}
]

average_age = sum(student["age"] for student in students) / len(students)
print("1. Average Age:")
print(average_age)


highest_grade_student = max(students, key=lambda x: x["grade"])["name"]
print("\n2. Student with Highest Grade is :")
print(highest_grade_student)


dictionary_of_ages = {student["name"]: student["age"] for student in students}
print("\n3. Dictionary of Ages:")
print(dictionary_of_ages)


set_of_tuples = {(student["name"], student["age"], student["grade"]) for student in students}
print("\n4. Set of Tuples:")
print(set_of_tuples)

sorted_students = sorted(students, key=lambda x: x["grade"], reverse=True)
print("\n5. Sorted Student Data:")
print(sorted_students)

