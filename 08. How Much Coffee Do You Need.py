coffee = 0
while True:
    command = input()

    if command == "END":
        break

    if command == "coding" or command == "dog" or command == "cat" or command == "movie":
        coffee += 1

    elif command == "CODING" or command == "DOG" or command == "CAT" or command == "MOVIE":
        coffee += 2
    else:
        continue

if coffee <= 5:
    print(coffee)
else:
    print(f"You need extra sleep")