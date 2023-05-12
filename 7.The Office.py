employees = [int(x) for x in input().split()]
factor = int(input())

av_happiness = 0

employees_hap = []

for x in employees:
    employees_hap.append(x * factor)
    av_happiness += x * factor
total_count = len(employees)
average_happiness = av_happiness // total_count
happy_count = 0

for i in employees_hap:
    if i > average_happiness:
        happy_count += 1

if happy_count >= len(employees) / 2:
    print(f"Score: {happy_count}/{total_count}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{total_count}. Employees are not happy!")


