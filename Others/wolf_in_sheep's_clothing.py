input_string = input()
lst = input_string.split(", ")
last_animal = lst[-1]
animal = 'wolf'
list_item_index = len(lst) - lst[::1].index(animal) - 1

if last_animal == "wolf":
    print("Please go away and stop eating my sheep")
elif last_animal == "sheep":
    print(f'Oi! Sheep number {list_item_index}! You are about to be eaten by a wolf!')