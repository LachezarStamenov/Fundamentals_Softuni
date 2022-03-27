gifts = input().split()
command = input()
while command != "No Money":
    current_command = command.split()
    current_gift = current_command[1]
    if current_command[0] == "OutOfStock":
        for current_index in range(len(gifts)):
            if gifts[current_index] == current_gift:
                gifts[current_index] = "None"
    elif current_command[0] == "Required":
        index = int(current_command[2])
        if 0 <= index < len(gifts):
            gifts[index] = current_gift
    elif current_command[0] == "JustInCase":
        gifts[-1] = current_gift
    command = input()
for gift in gifts:
    if gift != "None":
        print(gift, end=" ")
