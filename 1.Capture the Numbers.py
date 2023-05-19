import re

result = []

while True:
    line = input()
    if not line:
        break

    pattern = r"\d+"
    resul = re.findall(pattern, line)
    result.extend(resul)

print(" ".join(result))

