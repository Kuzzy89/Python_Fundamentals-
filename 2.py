lines = input().split("||")
fuel = int(input())
ammo = int(input())

for line in lines:
    command_arg = line.split()
    command = command_arg[0]
    #chislo = int(command_arg[1])

    if command == "Travel":
        chislo = int(command_arg[1])
        if chislo <= fuel:
            print(f"The spaceship travelled {chislo} light-years.")
            fuel -= chislo
        else:
            print(f"Mission failed.")
            exit()

    elif command == "Enemy":
        chislo = int(command_arg[1])
        if ammo >= chislo:
            print(f"An enemy with {chislo} armour is defeated.")
            ammo -= chislo
        else:
            if 2 * chislo <= fuel:
                print(f"An enemy with {chislo} armour is outmaneuvered.")
                fuel -= 2 * chislo
            else:
                print(f"Mission failed.")
                exit()

    elif command == "Repair":
        chislo = int(command_arg[1])
        ammo += 2 * chislo
        fuel += chislo
        ammo_added = 2 * chislo
        print(f"Ammunitions added: {ammo_added}.")
        print(f"Fuel added: {chislo}.")

    elif command == "Titan":
        print(f"You have reached Titan, all passengers are safe.")
        exit()

