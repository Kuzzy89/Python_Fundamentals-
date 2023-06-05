a = int(input())
b = int(input())

thousands = (a // 1000) % 10
hundreds = (a // 100) % 10
tens = (a // 10) % 10
units = (a % 10)

thousands_b = (b // 1000) % 10
hundreds_b = (b // 100) % 10
tens_b = (b // 10) % 10
units_b = (b % 10)

for num_1 in range(thousands, thousands_b + 1):
    for num_2 in range(hundreds, hundreds_b + 1):
        for num_3 in range(tens, tens_b + 1):
            for num_4 in range(units, units_b + 1):
                if num_1 % 2 != 0 and num_2 % 2 != 0 and num_3 % 2 != 0 and num_4 % 2 != 0:
                    print(f"{num_1}{num_2}{num_3}{num_4}", end=" ")