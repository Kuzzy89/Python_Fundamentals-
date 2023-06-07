row = int(input())
list_1 = []
counter = 0
for i in range(row):
    n = [int(x) for x in input().split()]
    list_1.append(n)

attack1 = input().split()

while attack1:

    attack = attack1[0].split("-")
    rows = int(attack[0])
    col = int(attack[1])

    for el in range(len(list_1)):
        if el == rows:
            columns = list_1[el]
            if columns[col] != 0:
                columns[col] -= 1
                if columns[col] == 0:
                    counter += 1

    attack1.pop(0)

print(counter)