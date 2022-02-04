def is_product_exist(lst, el):
    if el in lst:
        return True
    return False


initial_groceries_lst = input().split("!")

while True:
    command = input()
    token = command.split()
    action = token[0]
    product = token[1]
    if command == "Go Shopping!":
        break
    if action == "Urgent":
        if not is_product_exist(initial_groceries_lst, product):
            initial_groceries_lst.insert(0, product)

    elif action == "Unnecessary":
        if is_product_exist(initial_groceries_lst, product):
            initial_groceries_lst.remove(product)

    elif action == "Correct":
        if is_product_exist(initial_groceries_lst, product):
            initial_groceries_lst[initial_groceries_lst.index(product)] = token[2]

    elif action == "Rearrange":
        if is_product_exist(initial_groceries_lst, product):
            initial_groceries_lst.remove(product)
            initial_groceries_lst.append(product)

print(*initial_groceries_lst, sep=", ")