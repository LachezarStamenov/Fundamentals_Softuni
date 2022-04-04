# Write a program that receives info from the console about people and their phone numbers.
# Each entry should have a name and a number (both strings) separated by a "-". If you receive a name that already
# exists in the phonebook, update its number.
# After filling the phonebook, you will receive a number – N. Your program should be able to perform a search of contact
# by name and print its details in the format: "{name} -> {number}". In case the contact isn't found, print:' \
# "Contact {name} does not exist."


phone_book = {}

while True:

    command = input()
    if command.isnumeric():
        break
    name, number = command.split('-')
    phone_book[name] = number

for _ in range(int(command)):
    search_name = input()
    if search_name in phone_book:
        print(f"{search_name} -> {phone_book[search_name]}")
    else:
        print(f"Contact {search_name} does not exist.")

