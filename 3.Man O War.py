def is_idx_valid(idx, que):
    return 0 <= idx < len(que)


pirate_ship = [int(x) for x in input().split(">")]
war_ship = [int(x) for x in input().split(">")]

max_health = int(input())
is_running = True

while is_running:
    line = input()
    if line == "Retire":
        break

    com = line.split()

    if com[0] == "Fire":
        idx = int(com[1])
        damage = int(com[2])

        if not is_idx_valid(idx, war_ship):
            continue

        war_ship[idx] -= damage
        if war_ship[idx] <= 0:
            print("You won! The enemy ship has sunken.")
            is_running = False

    elif com[0] == "Defend":
        start_idx = int(com[1])
        end_idx = int(com[2])
        damage = int(com[3])

        if not is_idx_valid(start_idx, pirate_ship) or not is_idx_valid(end_idx, pirate_ship):
            continue

        for idx in range(start_idx, end_idx + 1):
            pirate_ship[idx] -= damage
            if pirate_ship[idx] <= 0:
                print(f"You lost! The pirate ship has sunken.")
                is_running = False
                break

    elif com[0] == "Repair":
        idx = int(com[1])
        health = int(com[2])
        if not is_idx_valid(idx, pirate_ship):
            continue

        pirate_ship[idx] = min(max_health, pirate_ship[idx] + health)
        # pirate_ship[idx] += health
        # if health > max_health:
        #     pirate_ship[idx] = max_health

    elif com[0] == "Status":
        counter = 0
        for i in pirate_ship:
            if i < max_health * 0.2:
                counter += 1

        print(f"{counter} sections need repair.")

pirate_ship_sum = sum(pirate_ship)
war_ship_sum = sum(war_ship)

if is_running:
    print(f"Pirate ship status: {pirate_ship_sum}\n"
          f"Warship status: {war_ship_sum}")
