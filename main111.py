word = input()

new = [i for i in word if i.lower() not in ['a', 'o', 'u', 'e', 'i']]

print("".join(new))