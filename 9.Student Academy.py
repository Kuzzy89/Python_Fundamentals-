n = int(input())
dictt = {}

for _ in range(n):
    student = input()
    grade = float(input())

    if student not in dictt:
        dictt[student] = []

    dictt[student].append(grade)

for student, grade in dictt.items():
    average_grades = sum(grade) / len(grade)
    if average_grades >= 4.5:
        print(f"{student} -> {average_grades:.2f}")

