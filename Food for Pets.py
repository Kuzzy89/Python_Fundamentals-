import math

days = int(input())
all_food = float(input())

eaten_dog_food = 0
eaten_cat_food = 0
biscuit = 0
all_eaten_food = 0
for i in range(1, days + 1):
    dog_food = int(input())
    cat_food = int(input())
    eaten_dog_food += dog_food
    eaten_cat_food += cat_food
    all_eaten_food += cat_food + dog_food

    if i % 3 == 0:
        biscuit = (cat_food + dog_food) * 0.1

print(f"Total eaten biscuits: {round(biscuit)}gr.")
print(f"{all_eaten_food/all_food * 100:.2f}% of the food has been eaten.")
print(f"{eaten_dog_food/all_eaten_food * 100:.2f}% eaten from the dog.")
print(f"{eaten_cat_food/all_eaten_food * 100:.2f}% eaten from the cat.")