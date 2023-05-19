import re


text = input()

pattern = r"\b_([A-Za-z\d]+)\b"

res = re.findall(pattern, text)
print(",".join(res))

