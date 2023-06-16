list_as_str = input().split()
list_int = []
for i in list_as_str:
    n = round(float(i))
    list_int.append(n)

print(list_int)