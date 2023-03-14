text = input()

for i in range(len(text)):
    ch = text[i]
    if ch == ":":
        symbol = text[i + 1]
        print(f":{symbol}")
