n = int(input())

for i in range(n):
    word = input()

    is_pure = True

    # for c in word:
    #

    for inx in range(len(word)):
        c = word[inx]
        if c == "." or c == "_" or c == ",":
            is_pure = False
            break

    if is_pure:
        print(f"{word} is pure.")

    else:
        print(f"{word} is not pure!")