n = int(input())

for i in range(1111, 10000):
    thousand = i // 1000 % 10
    hundred = i // 100 % 10
    ten = i // 10 % 10
    unit = i % 10
    if n % thousand == 0 and n % hundred == 0 and n % ten == 0 and n % unit == 0:
        print(f"{thousand}{hundred}{ten}{unit}", end=" ")

