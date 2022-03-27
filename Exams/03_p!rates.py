command = input()
cities_info = {}

while not command == "Sail":
    current_command = command.split('||')
    town = current_command[0]
    people, gold = int(current_command[1]), int(current_command[2])
    if town in cities_info:
        cities_info[town]['people'] += people
        cities_info[town]['gold'] += gold
    else:
        cities_info[town] = {'people': int(people), 'gold': int(gold)}

    command = input()

lines = input()

while not lines == 'End':
    current_line = lines.split('=>')
    action, town = current_line[0], current_line[1]

    if action == 'Plunder':
        people, gold = int(current_line[2]), int(current_line[3])
        cities_info[town]['people'] -= people
        cities_info[town]['gold'] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if cities_info[town]['people'] <= 0 or cities_info[town]['gold'] <= 0:
            del cities_info[town]
            print(f"{town} has been wiped off the map!")

    elif action == 'Prosper':
        gold = int(current_line[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities_info[town]['gold'] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities_info[town]['gold']} gold.")

    lines = input()

if len(cities_info) == 0:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")

else:
    print(f"Ahoy, Captain! There are {len(cities_info)} wealthy settlements to go to:")
    for city in cities_info.keys():
        print(f"{city} -> Population: {cities_info[city]['people']} citizens, Gold: {cities_info[city]['gold']} kg")