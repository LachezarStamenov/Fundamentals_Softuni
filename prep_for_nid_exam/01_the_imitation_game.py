decoded_msg = [letter for letter in input()]


while True:
    command = input().split('|')
    if command[0] == 'Decode':
        print(f"The decrypted message is: {''.join(decoded_msg)}")
        break

    if command[0] == 'Move':
        firstPart = decoded_msg[:int(command[1])]
        secondPart = decoded_msg[int(command[1]):len(decoded_msg)]
        decoded_msg = secondPart + firstPart
    if command[0] == 'Insert':
        firstPart = decoded_msg[:int(command[1])]
        secondPart = decoded_msg[int(command[1]):len(decoded_msg)]
        decoded_msg = firstPart + list(command[2]) + secondPart

    if command[0] == 'ChangeAll':
        decoded_msg[:] = [x if x != command[1] else command[2] for x in decoded_msg]