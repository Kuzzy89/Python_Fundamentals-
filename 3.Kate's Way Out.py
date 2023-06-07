rows = int(input())
maze = []
count = 0
for i in range(rows):
    n = input()
    maze.append([n])

while True:

    for el in range(len(maze[rows])):
        if el == " ":
            count += 1
            continue
        elif el == "#":
            print()


