budget = float(input())

flour = float(input())
pack_of_eggs = flour * 0.75
milk = (flour * 1.25) * 0.25

one_loaf_price = flour + pack_of_eggs + milk
colored_egg_counter = 0
loaf_counter = 0

while one_loaf_price <= budget:
    loaf_counter += 1
    budget -= one_loaf_price
    colored_egg_counter += 3

    if loaf_counter % 3 == 0:
        colored_egg_counter -= (loaf_counter - 2)

print(f"You made {loaf_counter} loaves of Easter bread! Now you have {colored_egg_counter} eggs and {budget:.2f}BGN left.")