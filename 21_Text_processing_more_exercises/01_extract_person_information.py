# Write a program that reads N lines of strings and extracts the name and the age of a given person:
# •	The person's name will be surrounded by "@" and "|" in the format "@{name}|".
# •	The person's age will be surrounded by "#" and "*" in the format "#{age}*".
# Example: "Hello my name is @Peter| and I am #20* years old."
# For each found name-age pair, print a line in the following format "{name} is {age} years old."

num_of_lines = int(input())
person = dict()
for i in range(num_of_lines):
    string = input()
    first_symbol_index = string.index("@")
    second_symbol_index = string.index("|")
    third_symbol_index = string.index("#")
    forth_symbol_index = string.index("*")

    name = string[first_symbol_index + 1: second_symbol_index]
    year = string[third_symbol_index + 1:forth_symbol_index]
    person[name] = year

for name, age in person.items():
    print(f"{name} is {age} years old.")