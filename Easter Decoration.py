clients = int(input())
all_money = 0

for i in range(clients):
    current_money_spend = 0
    current_items_count = 0

    while True:
        command = input()
        if command == "Finish":
            break

        if command == "basket":
            current_money_spend += 1.5
            current_items_count += 1

        elif command == "wreath":
            current_money_spend += 3.8
            current_items_count += 1

        elif command == "chocolate bunny":
            current_money_spend += 7
            current_items_count += 1

    if current_items_count % 2 == 0:
        current_money_spend -= current_money_spend * 0.2

    all_money += current_money_spend
    print(f"You purchased {current_items_count} items for {current_money_spend:.2f} leva.")
average = all_money / clients
print(f"Average bill per client is: {average:.2f} leva.")