# Write a program that prints the sum of all found characters between two given characters (their ASCII code). On each
# of the first two lines, you will receive a single character. On the last line, you get a random string. Print the sum
# of the ASCII values of all characters in the random string between the two given characters in the ASCII table.

first_char = ord(input())
second_char = ord(input())
random_string = input()

total_sum = 0

start = min(first_char, second_char)
end = max(first_char, second_char)

for i in range(len(random_string)):
    current_char = ord(random_string[i])
    if start < current_char < end:
        total_sum += int(current_char)

print(total_sum)