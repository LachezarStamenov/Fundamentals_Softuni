# Write a program that counts all characters in a string except for space (" ").
# Print all the occurrences in the following format:
# "{char} -> {occurrences}"

text = input()
line_dict = {}

for char in text:
    if char == " ":
        continue
    if char not in line_dict:
        line_dict[char] = 0
    line_dict[char] += 1


for (key, value) in line_dict.items():
    print(f"{key} -> {value}")