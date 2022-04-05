"""Write a program that reads usernames on a single line (separated by ", ") and prints all valid usernames on
separate lines.
A valid username:
•	has length between 3 and 16 characters inclusive
•	can contain only letters, numbers, hyphens, and underscores
•	has no redundant symbols before, after, or in between"""

string_as_list = input().split(", ")

for username in string_as_list:
    if 3 <= len(username) <= 16 and (username.isalnum() or "_" in username or "-" in username):
        print(username)

# решение на Марио
# import string
# def valid_username(data):
#     flag = 0
#     expected_elements = string.digits + string.ascii_letters + '_' + '-'
#     for name in data:
#         flag = 0
#         if 3> len(name) or len(name) > 16:
#             flag = 1
#         elif len([x for x in name if x in expected_elements]) != len(name):
#             flag = 1
#         elif flag == 0:
#             print(name)
#
# d = input().split(', ')
# valid_username(d)