def extract_func(command, data_dict: dict):
    command = command.split("||")
    town = command[0]
    population = int(command[1])
    gold = int(command[2])

    if town not in data_dict:
        data_dict[town] = [population, gold]
    else:
        data_dict[town][0] += population
        data_dict[town][1] += gold
    return data_dict


def sail_func(command, data_dict: dict):
    command = command.split("=>")
    current_command = command[0]
    if current_command == "Plunder":
        town = command[1]
        people = int(command[2])
        gold = int(command[3])

        killed = 0
        if data_dict[town][0] - people >= 0:
            killed = people
            data_dict[town][0] -= people
        else:
            killed = people - data_dict[town][0]
            data_dict[town][0] -= killed
        stolen_gold = 0
        if data_dict[town][1] - gold >= 0:
            stolen_gold = gold
            data_dict[town][1] -= gold
        else:
            stolen_gold = gold - data_dict[town][1]
            data_dict[town][1] -= stolen_gold
        print(f"{town} plundered! {stolen_gold} gold stolen, {killed} citizens killed.")
        if data_dict[town][0] <= 0 or data_dict[town][1] <= 0:
            del data_dict[town]
            print(f"{town} has been wiped off the map!")

    elif current_command == "Prosper":
        town = command[1]
        gold = int(command[2])

        if gold > 0:
            data_dict[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {data_dict[town][1]} gold.")
        else:
            print("Gold added cannot be a negative number!")

    return data_dict


def pirates():
    data_dict = {}
    condition = False
    while True:
        command = input()
        if command == "End":
            break

        elif command != "Sail" and not condition:
            data_dict = extract_func(command, data_dict)

        elif command == "Sail":
            condition = True
            continue

        elif condition:
            data_dict = sail_func(command, data_dict)
    print(f"Ahoy, Captain! There are {len(data_dict)} wealthy settlements to go to:")

    for data in data_dict:
        print(f"{data} -> Population: {data_dict[data][0]} citizens, Gold: {data_dict[data][1]} kg")


pirates()