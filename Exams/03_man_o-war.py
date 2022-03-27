def check_the_index_is_valid(lst, ind):
    if 0 <= ind < len(lst):
        return True
    else:
        return False


pirate_ship_status = list(map(int,input().split(">")))
war_ship_status = list(map(int,input().split(">")))
max_health = int(input())
game_over = False

command = input()

while not command == "Retire":
    current_command = command.split()
    action = current_command[0]

    if action == "Fire":
        index = int(current_command[1])
        reduction = int(current_command[2])
        if check_the_index_is_valid(war_ship_status, index):
            war_ship_status[index] -= reduction
            if war_ship_status[index] <= 0:
                print(f"You won! The enemy ship has sunken.")
                game_over = True
                break
    elif action == "Defend":
        start_ind = int(current_command[1])
        end_ind = int(current_command[2])
        reduction = int(current_command[3])

        if check_the_index_is_valid(pirate_ship_status, start_ind) and check_the_index_is_valid(pirate_ship_status, end_ind):
            for i in range(start_ind, end_ind + 1):
                pirate_ship_status[i] -= reduction
                if pirate_ship_status[i] <= 0:
                    print(f"You lost! The pirate ship has sunken.")
                    game_over = True
                    break
    elif action == "Repair":
        index = int(current_command[1])
        health = int(current_command[2])
        if check_the_index_is_valid(pirate_ship_status, index):
            pirate_ship_status[index] += health
            if pirate_ship_status[index] > max_health:
                pirate_ship_status[index] = max_health

    elif action == "Status":
        counter = 0
        for x in pirate_ship_status:
            if x < max_health * 0.2:
                counter += 1
        print(f'{counter} sections need repair.')

    command = input()

if not game_over:
    print(f'Pirate ship status: {sum(pirate_ship_status)}')
    print(f'Warship status: {sum(war_ship_status)}')