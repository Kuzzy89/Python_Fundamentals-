
def replace_char_code(word):
    char_code_str = ""
    new_word = []

    for ch in word:
        if ch.isnumeric():
            char_code_str += ch
        else:
            new_word.append(ch)

    ch_at_the_beginning = chr(int(char_code_str))
    new_word.insert(0, ch_at_the_beginning)

    return new_word


def decipher_word(word):

    new_word = replace_char_code(word)

    new_word[1], new_word[-1] = new_word[-1], new_word[1]

    return "".join(new_word)


words = input().split()
deciphered_word = [decipher_word(word) for word in words]
print(" ".join(deciphered_word))