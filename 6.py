n = int(input())
hund = n // 100 % 10
des = n // 10 % 10
unit = n % 10

for i in range(1, unit + 1):
    for j in range(1, des + 1):
        for x in range(1, hund + 1):
            total = i * j * x
            print(f"{i} * {j} * {x} = {total};")
