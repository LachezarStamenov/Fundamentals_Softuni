# On the first line, you will be given a string containing all of your stops. Until you receive the command "Travel",
# you will be given some commands to manipulate that initial string. The commands can be:
# •	"Add Stop:{index}:{string}":
# o	Insert the given string at that index only if the index is valid
# •	"Remove Stop:{start_index}:{end_index}":
# o	Remove the elements of the string from the starting index to the end index (inclusive) if both indices are valid
# •	"Switch:{old_string}:{new_string}":
# o	If the old string is in the initial string, replace it with the new one (all occurrences)
# Note: After each command, print the current state of the string
# After the "Travel" command, print the following: "Ready for world tour! Planned stops: {string}"
# Input / Constraints
# •	JavaScript: you will receive a list of strings
# •	An index is valid if it is between the first and the last element index (inclusive) in the sequence.
# Output
# •	Print the proper output messages in the proper cases as described in the problem description
# Examples

stops_as_str = input()
command = input()

while not command == "Travel":

    current_command = command.split(":")
    action = current_command[0]


    if action == "Add Stop":
        index = int(current_command[1])
        string = current_command[2]
        if 0 <= index < len(stops_as_str):
            stops_as_str = stops_as_str[0:index] + string + stops_as_str[index:]
        print(stops_as_str)

    elif action == "Remove Stop":
        start_index = int(current_command[1])
        end_index = int(current_command[2])
        if 0 <= start_index < len(stops_as_str) and 0 < end_index < len(stops_as_str):
            stops_as_str = stops_as_str[0:start_index] + stops_as_str[end_index+1:]
        print(stops_as_str)
    elif action == "Switch":
        old_string = current_command[1]
        new_string = current_command[2]
        if 0 < len(old_string) and 0 < len(stops_as_str):
            stops_as_str = stops_as_str.replace(old_string, new_string)
        print(stops_as_str)

    command = input()
print(f"Ready for world tour! Planned stops: {stops_as_str}")
