while True:
    line = input()
    if line == "End":
        break

    if line == "SoftUni":
        continue

    converted_word = ""
    for ch in line:
        converted_word += 2 * ch

        # print(f"{ch}{ch}", end="")
    print(converted_word)