cards = input().split()
n = int(input())

half = len(cards) // 2

for i in range(n):
    left_side = cards[0:half]
    right_side = cards[half:]

    faro_cars = []

    for j in range(len(left_side)):
        faro_cars.append(left_side[j])
        faro_cars.append(right_side[j])

    cards = faro_cars

print(cards)

