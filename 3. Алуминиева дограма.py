count_joinery = int(input())
kind_of_joinery = input()
transport = input()

price = 0

if kind_of_joinery == "90X130":
    price = 110 * count_joinery
    if count_joinery > 60:
        price -= price * 0.08
    elif count_joinery > 30:
        price -= price * 0.05

if kind_of_joinery == "100X150":
    price = 140 * count_joinery
    if count_joinery > 80:
        price -= price * 0.1
    elif count_joinery > 40:
        price -= price * 0.06

if kind_of_joinery == "130X180":
    price = 190 * count_joinery
    if count_joinery > 50:
        price -= price * 0.12
    elif count_joinery > 20:
        price -= price * 0.07

if kind_of_joinery == "200X300":
    price = 250 * count_joinery
    if count_joinery > 50:
        price -= price * 0.14
    elif count_joinery > 25:
        price -= price * 0.09

if transport == "With delivery":
    price += 60

if count_joinery > 99:
    price -= price * 0.04

if count_joinery < 10:
    print("Invalid order")
else:
    print(f"{price:.2f} BGN")
