def merge_element(elements, start, end):
    merge_result = ""
    for i in range(start, end + 1):
        merge_result += elements[i]

    return merge_result


words = input().split()

while True:
    line = input()
    if line == "3:1":
        break

    command, first_arg, sec_arg = line.split()

    if command == "merge":
        start_idx = int(first_arg)
        end_idx = int(sec_arg)

        start_idx = max(0, start_idx)
        end_idx = min(len(words) - 1, end_idx)

        merged_element = merge_element(words, start_idx, end_idx)
        remove_count_ops = end_idx - start_idx + 1
        for _ in range(remove_count_ops):
            words.pop(start_idx)
        words.insert(start_idx, merged_element)

    elif command == "divide":
        el_idx = int(first_arg)
        partition = int(sec_arg)

        element = words[el_idx]
        elements_part = []
        partition_size = len(element) // partition

        current_partition = ""
        for inx in range((partition - 1) * partition_size):
            current_partition += element[inx]

            if len(current_partition) == partition_size:
                elements_part.append(current_partition)
                current_partition = ""

        current_partition = ""
        for idx in range((partition - 1) * partition_size, len(element)):
            current_partition += element[idx]

        elements_part.append(current_partition)

        words.pop(el_idx)

        for idx in range(len(elements_part)):
            words.insert(el_idx + idx, elements_part[idx])

print(" ".join(words))