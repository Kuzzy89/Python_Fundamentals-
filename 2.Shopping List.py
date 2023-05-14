# def find_idx_by_el(seq, el):
#     for el_idx in range(len(seq)):
#         if seq[el_idx] == el:
#             return el_idx
#
#     return -1


product_list = input().split("!")

while True:
    line = input()
    if line == "Go Shopping!":
        break

    command_args = line.split()
    command = command_args[0]
    product = command_args[1]

    if command == "Urgent":
        if product not in product_list:
            product_list.insert(0, product)

    elif command == "Unnecessary":
        if product in product_list:
            product_list.remove(product)

    elif command == "Correct":
        new_product = command_args[2]
        if product in product_list:
            idx = product_list.index(product)
            product_list[idx] = new_product

        # idx = find_idx_by_el(product_list, product)
        # if idx == - 1:
        #     continue
        # product_list[idx] == new_product

    elif command == "Rearrange":
        if product in product_list:
            product_list.remove(product)
            product_list.append(product)

print(", ".join(product_list))