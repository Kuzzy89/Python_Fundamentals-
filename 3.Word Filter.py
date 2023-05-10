# list1 = [x for x in input().split() if len(x) % 2 == 0]
#
# print("\n".join(list1))

list1 = input().split()

result = list(filter(lambda x: len(x) % 2 == 0, list1))
print(result)