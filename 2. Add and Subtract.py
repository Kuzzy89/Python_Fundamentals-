def sum_numbers(a, b):
    result = a + b

    return result


def subtract(a, b):
    result = a - b

    return result


n1 = int(input())
n2 = int(input())
n3 = int(input())

print(subtract(sum_numbers(n1, n2), n3))