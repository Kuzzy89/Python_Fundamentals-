word = input()

re_word = ""
for i in range(len(word) -1, -1, -1):
    re_word += word[i]
print(re_word)