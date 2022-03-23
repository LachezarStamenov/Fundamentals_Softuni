# You are a pianist, and you like to keep a list of your favorite piano pieces. Create a program to help you organize
# it and add, change, remove pieces from it!
# On the first line of the standard input, you will receive an integer n – the number of pieces you will initially have.
# On the next n lines, the pieces themselves will follow with their composer and key, separated by "|" in the following
# format: "{piece}|{composer}|{key}".
# Then, you will be receiving different commands, each on a new line, separated by "|", until the "Stop" command is
# given:
# •	"Add|{piece}|{composer}|{key}":
# o	You need to add the given piece with the information about it to the other pieces and print:
# "{piece} by {composer} in {key} added to the collection!"
# o	If the piece is already in the collection, print:
# "{piece} is already in the collection!"
# •	"Remove|{piece}":
# o	If the piece is in the collection, remove it and print:
# "Successfully removed {piece}!"
# o	Otherwise, print:
# "Invalid operation! {piece} does not exist in the collection."
# •	"ChangeKey|{piece}|{new key}":
# o	If the piece is in the collection, change its key with the given one and print:
# "Changed the key of {piece} to {new key}!"
# o	Otherwise, print:
# "Invalid operation! {piece} does not exist in the collection."
# Upon receiving the "Stop" command, you need to print all pieces in your collection, sorted by their name and by the
# name of their composer in alphabetical order, in the following format:
# "{Piece} -> Composer: {composer}, Key: {key}"
# Input/Constraints
# •	You will receive a single integer at first – the initial number of pieces in the collection
# •	For each piece, you will receive a single line of text with information about it.
# •	Then you will receive multiple commands in the way described above until the command "Stop".
# Output
# •	All the output messages with the appropriate formats are described in the problem description.

def add_piece(collection_dict, composer, key, piece):
        if piece in collection_dict:
            print(f"{piece} is already in the collection!")
        else:
            collection_dict[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
        return collection_dict

def remove_piece(collection_dict, piece):
    if piece in collection_dict:
        del collection_dict[piece]
        print(f"Successfully removed {piece}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")
    return collection_dict


def change_key(collection_dict,piece, new_key):
    if piece in collection:
        collection[piece][1] = new_key
        print(f"Changed the key of {piece} to {new_key}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")
    return collection_dict

n = int(input())

collection = {}

for i in range(n):
    text_input = input().split('|')
    piece = text_input[0]
    composer = text_input[1]
    key = text_input[2]
    collection[piece] = [composer, key]

command = input()

while not command == "Stop":

    command = command.split('|')
    type_command = command[0]
    piece = command[1]

    if type_command == 'Add':
        composer = command[2]
        key = command[3]
        add_piece(collection, composer, key, piece)

    elif type_command == 'Remove':
        remove_piece(collection, piece)

    elif type_command == 'ChangeKey':
        new_key = command[2]
        change_key(collection, piece, new_key)


    command = input()

for piece in collection:
    print(f"{piece} -> Composer: {collection[piece][0]}, Key: {collection[piece][1]}")
