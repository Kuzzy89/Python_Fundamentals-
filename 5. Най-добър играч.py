import sys

max_goals = - sys.maxsize
current_name = ""
max_name = ""

name = input()
while name != "END":
    goals = int(input())
    current_name = name

    if goals > max_goals:
        max_goals = goals
        max_name = current_name

    if goals >= 10:
        break

    name = input()
print(f"{max_name} is the best player!")
if max_goals >= 3:
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
elif max_goals < 3:
    print(f'He has scored {max_goals} goals.')




