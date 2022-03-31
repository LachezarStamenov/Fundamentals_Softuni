# Write a program that prints all elements from a given sequence of words that occur an odd number of times
# (case-insensitive) in it.
# •	Words are given on a single line, space-separated.
# •	Print the result elements in lowercase, in their order of appearance.

line = input().lower().split(' ')
line_dict = {}

for word in line:
    if word not in line_dict:
        line_dict[word] = 0
    line_dict[word] += 1

output = [key for key, value in line_dict.items() if value % 2 != 0]
print(*output, sep=' ')