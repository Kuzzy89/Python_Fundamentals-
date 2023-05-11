electrons = int(input())
result = []

while electrons > 0:
    n = len(result) + 1

    shell_values = min(2 * (n ** 2), electrons)
    result.append(shell_values)
    electrons -= shell_values

print(result)