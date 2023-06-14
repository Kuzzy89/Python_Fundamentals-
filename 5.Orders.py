

def calc(prod, quant):
    price = 0
    if prod == "coffee":
        price = quant * 1.5
    elif prod == "coke":
        price = quant * 1.4
    elif prod == "water":
        price = quant * 1
    elif prod == "snacks":
        price = quant * 2

    return price


product = input()
quantity = int(input())
res = calc(product, quantity)
print(f"{res:.2f}")