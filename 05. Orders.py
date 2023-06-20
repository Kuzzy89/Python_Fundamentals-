number_of_orders = int(input())
total_price = 0

for i in range(number_of_orders):
    price_of_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())

    if price_of_capsule < 0.01 or price_of_capsule > 100:
        continue

    if days < 1 or days > 31:
        continue

    if capsules_needed_per_day < 1 or capsules_needed_per_day > 2000:
        continue

    current_price = price_of_capsule * capsules_needed_per_day * days
    total_price += current_price
    print(f"The price for the coffee is: ${current_price:.2f}")

print(f"Total: ${total_price:.2f}")