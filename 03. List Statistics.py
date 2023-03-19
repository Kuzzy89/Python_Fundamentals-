n = int(input())

neg = []
pos = []

for i in range(n):
    nums = int(input())
    if nums >= 0:
        pos.append(nums)

    else:
        neg.append(nums)

print(pos)
print(neg)
print(f"Count of positives: {len(pos)}")
print(f"Sum of negatives: {sum(neg)}")