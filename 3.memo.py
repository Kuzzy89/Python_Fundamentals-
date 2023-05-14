def is_it_in_boundary(start_index, bound):
    if 0 <= start_index < bound:
        return True
    return False


def is_number_valid(ind1, ind2, bound):
    if(is_it_in_boundary(ind1, bound)) and (is_it_in_boundary(ind2, bound)) and ind1 != ind2:
        return True
    return False


numbers = input().split()

command = input()
counter = 0

while command != "end":
    index1, index2 = [int(x) for x in command.split()]
    counter += 1

    if is_number_valid(index1, index2, len(numbers)):

        if numbers[index1] == numbers[index2]:
            element = numbers[index1]
            numbers.remove(element)
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
print(" ".join(numbers))