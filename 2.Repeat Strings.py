strings = input().split()
result = ""

for word in strings:
    result += len(word) * word

print(result)
