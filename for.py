n = int(input())
nums = 0
for i in range(1, n + 1):
    numbers = int(input())
    nums += numbers
last = nums / n
print(f"{last:.2f}")