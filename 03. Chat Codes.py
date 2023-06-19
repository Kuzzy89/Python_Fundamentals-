n = int(input())

for i in range(n):
    number = int(input())
    if number == 88:
        print(f"Hello")
    elif number == 86:
        print(f"How are you?")
    elif number < 88 and number != 86:
        print(f"GREAT!")
    elif number > 88:
        print(f"Bye.")
