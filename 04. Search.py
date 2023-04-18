n = int(input())
word = input()
list_word = []

for i in range(n):
    new_word = input()
    list_word.append(new_word)
print(list_word)

for i in range(len(list_word) - 1, -1, -1):
    element = list_word[i]
    if word not in element:
        list_word.remove(element)
print(list_word)


