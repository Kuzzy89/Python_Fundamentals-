phonebook = {}
while True:
    c_line = input()
    if "-" not in c_line:
        break

    key, value = c_line.split("-")
    phonebook[key] = value

for i in range(int(c_line)):
    new_key = input()
    if new_key in phonebook:
        print(f"{new_key} -> {phonebook[new_key]}")
    else:
        print(f"Contact {new_key} does not exist.")