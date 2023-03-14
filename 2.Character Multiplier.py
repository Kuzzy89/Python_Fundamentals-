words = input().split()
first_word = words[0]
second_word = words[1]

min_len = min(len(first_word), len(second_word))
result = 0

for i in range(min_len):
    first_word_char = first_word[i]
    second_word_char = second_word[i]
    result += ord(first_word_char) * ord(second_word_char)

for i in range(min_len, len(first_word)):
    result += ord(first_word[i])

for i in range(min_len, len(second_word)):
    result += ord(second_word[i])

print(result)