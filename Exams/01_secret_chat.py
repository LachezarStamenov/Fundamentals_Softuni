def insert_space(message, inx):
    message = message[:inx] + " " + message[inx:]
    return message


def reverse(message, substring):

    if substring not in message:
        print("error")
    else:
        message = message.replace(substring, "", 1)
        message = message + substring[::-1]
        print(message)
    return message


def change_all(message, substring, replacement):
    message = message.replace(substring, replacement)
    return message


concealed_message = input()
command = input()

while not command == "Reveal":
    current_command = command.split(":|:")
    action = current_command[0]

    if action == "InsertSpace":
        index = int(current_command[1])
        concealed_message = insert_space(concealed_message, index)
        print(concealed_message)
    elif action == "Reverse":
        sub_string = current_command[1]
        concealed_message = reverse(concealed_message, sub_string)

    elif action == "ChangeAll":
        sub_string = current_command[1]
        replacement = current_command[2]
        concealed_message = change_all(concealed_message, sub_string, replacement)
        print(concealed_message)

    command = input()

print(f"You have a new text message: {concealed_message}")