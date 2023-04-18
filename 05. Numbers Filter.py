n = int(input())
even = []
odd = []
negative = []
positive = []

for i in range(n):
    number = int(input())
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

    if number >= 0:
        positive.append(number)
    else:
        negative.append(number)

command = input()
if command == "even":
    print(even)
if command == "odd":
    print(odd)
if command == "negative":
    print(negative)
if command == "positive":
    print(positive)
