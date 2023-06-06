line = [int(x) for x in input().split(", ")]
list_0 = []
list_1 = []

for x in line:
    if x == 0:
        list_0.append(x)
    else:
        list_1.append(x)

print(list_1 + list_0)
