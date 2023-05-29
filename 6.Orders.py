products = {}

while True:
    line = input()
    if line == "buy":
        break
    command = line.split()
    name = command[0]
    price = float(command[1])
    quantity = int(command[2])

    if name in products:
        products[name] = [price, (quantity + products[name][1])]
    else:
        products[name] = [price, quantity]

for k in products:
    total_sum = products[k][0] * products[k][1]
    print(f"{k} -> {total_sum:.2f}")

