MAX_HEALTH = 100
health = MAX_HEALTH
initial_bitcoins = 0

rooms = input().split("|")
is_alive = True
counter = 0

for room in rooms:
    command, amount = room.split()
    amount = int(amount)
    counter += 1

    if command == "potion":
        if health + amount > MAX_HEALTH:
            print(f"You healed for {MAX_HEALTH - health} hp.")
            health = MAX_HEALTH
        else:
            health += amount
            print(f"You healed for {amount} hp.")

        print(f"Current health: {health} hp.")

    elif command == "chest":
        initial_bitcoins += amount
        print(f"You found {amount} bitcoins.")

    else:
        health -= amount
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {counter}")
            is_alive = False
            break

if is_alive:
    print(f"You've made it!")
    print(f"Bitcoins: {initial_bitcoins}")
    print(f"Health: {health}")