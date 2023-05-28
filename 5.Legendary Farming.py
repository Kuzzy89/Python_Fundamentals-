key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}
item_obtained = ""

while item_obtained == "":
    current_line = input().split()

    for i in range(0, len(current_line), 2):
        value = int(current_line[i])
        key = current_line[i + 1].lower()
        if key == "shards" or key == "fragments" or key == "motes":
            key_materials[key] += value

        elif key not in junk:
            junk[key] = value
        else:
            junk[key] += value

        if key_materials["shards"] >= 250:
            item_obtained = "Shadowmourne"
            print(f"{item_obtained} obtained!")
            key_materials["shards"] -= 250
            break
        elif key_materials["fragments"] >= 250:
            item_obtained = "Valanyr"
            key_materials["fragments"] -= 250
            print(f"{item_obtained} obtained!")
            break
        elif key_materials["motes"] >= 250:
            item_obtained = "Dragonwrath"
            key_materials["motes"] -= 250
            print(f"{item_obtained} obtained!")
            break

for key, value in key_materials.items():
    print(f"{key}: {value}")

# for key, value in junk.items():
#     print(f"{key}: {value}")