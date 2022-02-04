def check_if_item_in_the_chest(lst, item):
    if item in lst:
        return True
    else:
        return False


def check_if_the_index_is_valid(lst, index):
    if 0 <= index < len(lst):
        return True
    else:
        return False


loot_of_treasure = input().split("|")

command = input()
sum_items = 0


while not command == "Yohoho!":
    current_command = command.split()
    action = current_command[0]

    if action == "Loot":
        for item in current_command[1::]:
            if not check_if_item_in_the_chest(loot_of_treasure, item):
                loot_of_treasure.insert(0, item)

    elif action == "Drop":
        index = int(current_command[1])
        if check_if_the_index_is_valid(loot_of_treasure, index):
            el = loot_of_treasure.pop(index)
            loot_of_treasure.append(el)

    elif action == "Steal":
        count = int(current_command[1])

        if count >= len(loot_of_treasure):
            removed = loot_of_treasure
            print(', '.join(removed))
            print('Failed treasure hunt.')
            exit()
        else:
            removed = loot_of_treasure[-count:]
            del loot_of_treasure[-count:]
            print(', '.join(removed))

    command = input()


if len(loot_of_treasure)> 0:
    for item in loot_of_treasure:
        for i in item:
            sum_items += 1
# if len(loot_of_treasure) > 0:
#     for i in range(len(loot_of_treasure)):
#         sum_items += len(loot_of_treasure[i])

avg = f'{sum_items/len(loot_of_treasure):.2f}'
print(f'Average treasure gain: {avg} pirate credits.')
