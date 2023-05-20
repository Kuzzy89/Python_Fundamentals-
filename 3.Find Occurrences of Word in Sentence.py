import re

text = input().lower()
target = input().lower()

matches = re.findall(f'\\b{target}\\b', text)

print(len(matches))

