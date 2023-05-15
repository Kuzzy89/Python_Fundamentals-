def is_index_in_range(idx, cards_num):
    if 0 <= idx < len(cards_num):
        return True
    return False


def check_index_valid(p, o, cards_num):
    if (is_index_in_range(p, cards_num)) and (is_index_in_range(o, cards_num)) and o != p:
        return True
    return False


numbers = input().split()

command = input()
counter = 0
while command != "end":
    index1, index2 = [int(el) for el in command.split()]
    counter += 1

    if check_index_valid(index1, index2, numbers):

        if numbers[index1] == numbers[index2]:
            element = numbers[index1]
            numbers.pop(index1) #може да се използва и numbers.remove(element), след pop елементите се пренареждат
            numbers.remove(element)
            print(f"Congrats! You have found matching elements - {element}!")
        else:
            print(f"Try again!")

    else:
        element_to_add = f"-{counter}a"
        index = len(numbers) // 2
        numbers.insert(index, element_to_add)
        numbers.insert(index, element_to_add)
        print(f"Invalid input! Adding additional elements to the board")

    if not numbers:
        print(f"You have won in {counter} turns!")
        exit(0)

    command = input()

print(f"Sorry you lose :(")
print(*numbers, sep=" ") #може и с " ".join(numbers)