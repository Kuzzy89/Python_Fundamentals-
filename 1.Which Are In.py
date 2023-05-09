list1 = input().split(", ")
list2 = input().split(", ")

result = []
for subst in list1:
    for word in list2:
        found_subst = subst in word
        if found_subst:
            result.append(subst)
            break

print(result)