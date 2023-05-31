dicts = {}
while True:
    line = input()
    if line == "End":
        break

    company_name, emp_id = line.split("->")

    if company_name not in dicts:
        dicts[company_name] = []

    if emp_id not in dicts[company_name]:
        dicts[company_name].append(emp_id)

for key, value in dicts.items():
    print(key)
    for emp in value:
        print(f"--{emp}")


