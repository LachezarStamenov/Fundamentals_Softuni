dungeons_rooms = [el.split() for el in input().split("|")]

initial_health = 100
initial_bitcoins = 0
current_health = initial_health
current_bitcoins = initial_bitcoins
is_alive = True
room_num = 0

for room in dungeons_rooms:
    room_num += 1
    command = room[0]
    number = int(room[1])
    if command == "potion":

        if current_health + number > initial_health:
            number = initial_health - current_health
            current_health = initial_health
        else:
            current_health += number
        print(f"You healed for {number} hp.")
        print(f"Current health: {current_health} hp.")
    elif command == "chest":
        current_bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        current_health -= number
        if current_health > 0:
            print(f"You slayed {command}.")
        else:
            is_alive = False
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room_num}")
            break

if is_alive:
    print("You've made it!")
    print(f"Bitcoins: {current_bitcoins}")
    print(f"Health: {current_health}")







