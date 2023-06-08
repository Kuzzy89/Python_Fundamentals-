a = int(input())
b = int(input())
c = int(input())

new_list = [a, b, c]
zero = False
counter = 0

for i in range(len(new_list)):
    if a == 0 and b == 0 and c == 0:
        zero = True
        break

    elif new_list[i] < 0:
        counter += 1

if counter == 1 or counter == 3:
    print("negative")
elif zero:
    print("zero")
else:
    print("positive")