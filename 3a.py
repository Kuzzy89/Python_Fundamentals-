shelf_books = input().split("&")
#
helper1 = 0
helper2 = 0

while True:
    commands = input().split(" | ")
    if commands[0] == "Done":
        break
    if commands[0] == "Add Book":
        if commands[1] in shelf_books:
            continue
        else:
            shelf_books.insert(0, commands[1])
    if commands[0] == "Take Book":
        if commands[1] in shelf_books:
            shelf_books.remove(commands[1])
        else:
            continue
    if commands[0] == "Swap Books":
        if commands[1] in shelf_books and commands[2] in shelf_books:
            for x in range(len(shelf_books)):
                if shelf_books[x] == commands[1]:
                    helper1 = x
                if shelf_books[x] == commands[2]:
                    helper2 = x
            shelf_books[helper1] = commands[2]
            shelf_books[helper2] = commands[1]
        else:
            continue
    if commands[0] == "Insert Book":
        if commands[1] in shelf_books:
            continue
        else:
            shelf_books.append(commands[1])
    if commands[0] == "Check Book":
        commands[1] = int(commands[1])
        if 0 <= commands[1] < len(shelf_books):
            print(shelf_books[commands[1]])
        else:
            continue
print(", ".join(shelf_books))