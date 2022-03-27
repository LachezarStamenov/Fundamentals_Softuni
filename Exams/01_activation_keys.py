""" You are about to make some good money, but first, you need to think of a way to verify who paid for your product
and who didn't. You have decided to let people use the software for a free trial period and then require an activation
 key to continue using the product. Before you can cash out, the last step is to design a program that creates unique
  activation keys for each user. So, waste no more time and start typing!
The first line of the input will be your raw activation key. It will consist of letters and numbers only.
After that, until the "Generate" command is given, you will be receiving strings with instructions for different
operations that need to be performed upon the raw activation key.
There are several types of instructions, split by ">>>":
•	"Contains>>>{substring}":
o	If the raw activation key contains the given substring, prints: "{raw activation key} contains {substring}".
o	Otherwise, prints: "Substring not found!"
•	"Flip>>>Upper/Lower>>>{startIndex}>>>{endIndex}":
o	Changes the substring between the given indices (the end index is exclusive) to upper or lower case and then prints
the activation key.
o	All given indexes will be valid.
•	"Slice>>>{startIndex}>>>{endIndex}":
o	Deletes the characters between the start and end indices (the end index is exclusive) and prints the activation key.
o	Both indices will be valid.
Input
•	The first line of the input will be a string consisting of letters and numbers only.
•	After the first line, until the "Generate" command is given, you will be receiving strings.
Output
•	After the "Generate" command is received, print:
o	"Your activation key is: {activation key}"
"""

data = input()

command = input()

while not command == "Generate":
    current_command = command.split(">>>")
    action = current_command[0]

    if action == "Contains":
        substring = current_command[1]
        if substring in data:
            print(f"{data} contains {substring}")
        else:
            print("Substring not found!")

    elif action == "Flip":
        size = current_command[1]
        start_idx = int(current_command[2])
        end_idx = int(current_command[3])
        if size == "Upper":
            data = data[:start_idx] + data[start_idx: end_idx].upper() + data[end_idx:]
        elif size == "Lower":
            data = data[:start_idx] + data[start_idx: end_idx].lower() + data[end_idx:]
        print(data)
    elif action == 'Slice':
        start_idx = int(current_command[1])
        end_idx = int(current_command[2])
        data = data[:start_idx] + data[end_idx:]
        print(data)
    command = input()

print(f"Your activation key is: {data}")
