from math import ceil

number_of_the_students = int(input())
number_of_the_lectures = int(input())
additional_bonus = int(input())
max_bonus = 0
max_attendances = 0

for _ in range(1, number_of_the_students + 1):
    student_attendances = int(input())
    total_bonus = (student_attendances) / (number_of_the_lectures) * (5 + additional_bonus)
    if max_bonus < total_bonus:
        max_bonus = total_bonus

    if max_attendances < student_attendances:
        max_attendances = student_attendances

mak = ceil(max_bonus)
print(f"Max Bonus: {mak}.")
print(f"The student has attended {max_attendances} lectures.")