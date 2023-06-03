shelf = input().split("&")

help1 = 0
help2 = 0
while True:
    line = input()
    if line == "Done":
        break

    command_args = line.split(" | ")
    command = command_args[0]
    book = command_args[1]

    if command == "Add Book":
        if book in shelf:
            continue
        else:
            shelf.insert(0, book)

    elif command == "Take Book":
        if book in shelf:
            shelf.remove(book)

    elif command == "Swap Books":
        new_book = command_args[2]
        if new_book in shelf and book in shelf:

            for x in range(len(shelf)):
                if shelf[x] == book:
                    help1 = x
                if shelf[x] == new_book:
                    help2 = x
            shelf[help1] = new_book
            shelf[help2] = book
        else:
            continue

    elif command == "Insert Book":
        if book in shelf:
            continue
        else:
            shelf.append(book)
    elif command == "Check Book":
        book = int(book)
        if 0 <= book < len(shelf):
            print(shelf[book])
        else:
            continue


print(", ".join(shelf))