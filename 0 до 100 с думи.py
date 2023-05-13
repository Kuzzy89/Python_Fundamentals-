a = int(input())
if a <= 9:
    if a // 1 == 1:
        print("one")
    elif a // 2 == 1:
        print("two")
    elif a // 3 == 1:
        print("three")
    elif a // 4 == 1:
        print("four")
    elif a // 5 == 1:
        print("five")
    elif a // 6 == 1:
        print("six")
    elif a // 7 == 1:
        print("seven")
    elif a // 8 == 1:
        print("eight")
    elif a // 9 == 1:
        print("nine")

elif 10 <= a <= 99:
    if a / 10 == 2:
        print("twenty")
    elif a / 10 == 3:
        print("thirty")
    elif a / 10 == 4:
        print("forty")