num = input()


def calc(n):
    even = 0
    odd = 0

    for i in n:
        digit = int(i)

        if digit % 2 == 0:
            even += digit
        else:
            odd += digit

    return print(f"Odd sum = {odd}, Even sum = {even}")


(calc(num))
