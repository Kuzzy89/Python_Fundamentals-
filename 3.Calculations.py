def calc(oper, a, b):
    result = 0
    if oper == "multiply":
        result = a * b
    elif oper == "divide":
        result = a // b
    elif oper == "add":
        result = a + b
    elif oper == "subtract":
        result = a - b

    return result


operator = input()
n1 = int(input())
n2 = int(input())

print(calc(operator, n1, n2))
