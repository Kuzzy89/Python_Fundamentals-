wagons = int(input())
command = input()
train = [0] * wagons

while command != "End":
    action = command.split()[0]
    if action == "add":
        people = int(command.split()[1])
        train[-1] += people
    elif action == "insert":
        index = int(command.split()[1])
        people = int(command.split()[2])
        train[index] += people
    elif action == "leave":
        index = int(command.split()[1])
        people = int(command.split()[2])
        train[index] -= people

    command = input()

print(train)