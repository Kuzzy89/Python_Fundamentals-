text = input()

encrypt = ""
for ch in text:
    new_value = ord(ch) + 3
    encrypt += chr(new_value)

print(encrypt)