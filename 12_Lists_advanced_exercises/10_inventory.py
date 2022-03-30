def is_item_exist(item_lists, item):
    if item in item_lists:
        return True
    return False


def add_item(item_lists, item):
    if not is_item_exist(item_lists, item):
        item_lists.append(item)
    return item_lists


def remove_item(item_lists, item):
    if is_item_exist(item_lists, item):
        item_lists.remove(item)
    return item_lists


def combine_item(item_lists, items_data):
    old_item, new_item = items_data.split(":")
    if is_item_exist(item_lists, old_item):
        index_old_item = item_lists.index(old_item)
        item_lists.insert(index_old_item + 1, new_item)
    return item_lists


def renew_item(item_lists, item):
    if is_item_exist(item_lists, item):
        item_lists.remove(item)
        item_lists.append(item)
    return item_lists


items = input().split(", ")
command_input = input()

while not command_input == "Craft!":
    command, item = command_input.split(" - ")

    if command == "Collect":
        add_item(items, item)
    elif command == "Drop":
        remove_item(items, item)
    elif command == "Combine Items":
        combine_item(items, item)
    elif command == "Renew":
        renew_item(items, item)

    command_input = input()

print(*items, sep=", ")
