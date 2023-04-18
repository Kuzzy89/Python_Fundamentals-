numbers = input().split()
n = int(input())

int_nums = []

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

for i in range(n):

    min_elements = min(numbers)
    numbers.remove(min_elements)

for i in range(len(numbers)):
    numbers[i] = str(numbers[i])

print(", ".join(numbers))
