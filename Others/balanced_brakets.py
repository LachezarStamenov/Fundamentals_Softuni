numbers = int(input())
left_brackets = 0
right_brackets = 0
previous_command = ")"

for num in range(numbers):
    command = input()
    if command == "(":
        left_brackets += 1
    elif command == ")":
        right_brackets += 1
if previous_command == command:
    previous_command = command
    print("UNBALANCED")
if left_brackets == right_brackets:
    print("BALANCED")
else:
    print("UNBALANCED")


# n = int(input())
# previous_bracket = ")"
# is_balanced = True
# for _ in range(n):
#     data = input()
#     if data == chr(40) or data == chr(41):
#         if not previous_bracket == data:
#             previous_bracket = data
#         else:
#             previous_bracket = data
#             is_balanced = False
#             print("UNBALANCED")
#             break
#
# if is_balanced:
#     print("BALANCED")