food = int(input()) * 1000
command = input()
all_eaten_food_by_dog = 0

while command != "Adopted":
    eaten_food = int(command)
    all_eaten_food_by_dog += eaten_food

    command = input()

if all_eaten_food_by_dog <= food:
    print(f"Food is enough! Leftovers: {food - all_eaten_food_by_dog} grams.")
else:
    print(f"Food is not enough. You need {all_eaten_food_by_dog - food} grams more.")