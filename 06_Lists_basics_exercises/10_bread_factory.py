day_events_list = input().split("|")

max_energy = 100
order_energy = 30
rest_energy = 50
energy = 100
coins = 100
is_not_bankrupt = True

for event in day_events_list:
    single_events_list = event.split("-")
    name = single_events_list[0]
    value = int(single_events_list[1])

    if name == "rest":
        gained_energy = 0

        if energy + value > max_energy:
            gained_energy = max_energy - energy
            energy = max_energy
        else:
            energy += value
            gained_energy = value

        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")

    elif name == "order":
        if energy >= order_energy:
            energy -= order_energy
            coins += value
            print(f"You earned {value} coins.")
        else:
            energy += rest_energy
            print("You had to rest!")
            continue

    else:
        if coins > value:
            coins -= value
            print(f"You bought {name}.")
        else:
            print(f"Closed! Cannot afford {name}.")
            is_not_bankrupt = False
            break

if is_not_bankrupt:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")