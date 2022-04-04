#
# contests = {}  # contests {contest {username:points} }
# users = {}  # users {username: total_points}
#
# while True:
#     input_line = input()
#     if input_line == 'no more time':
#         break
#
#     username, contest, points = input_line.split(' -> ')
#
#     if username not in users:
#         users[username] = 0
#
#     if contest in contests:
#         if username in contests[contest]:
#             current_points = contests[contest][username]
#             contests[contest][username] = max(current_points, int(points))
#             if current_points == int(points):
#                 users[username] += current_points
#             else:
#                 users[username] += max(current_points, int(points)) - current_points
#         else:
#             contests[contest][username] = int(points)
#             users[username] += int(points)
#     else:
#         contests[contest] = {username: int(points)}
#         users[username] += int(points)
#
# for contest in contests.keys():
#     ranking = [rank for rank in sorted(contests[contest].items(), key=lambda item: (-item[1], item[0]))]
#     output = [f'{i + 1}. {name} <::> {points}' for i, (name, points) in enumerate(ranking)]
#     print(f"{contest}: {len(output)} participants")
#     print(*output, sep='\n')
#
# user_ranking = [rank for rank in sorted(users.items(), key=lambda item: (-item[1], item[0]))]
# output = [f'{i + 1}. {name} -> {points}' for i, (name, points) in enumerate(user_ranking)]
# print("Individual standings:")
# print(*output, sep='\n')

command = input()
contests_info = {}
users_info = {}

while not command == "no more time":
    data = command.split(" -> ")
    user_name = data[0]
    contest = data[1]
    points = int(data[2])

    if contest not in contests_info:
        contests_info[contest] = {}
    if user_name not in contests_info[contest]:
        contests_info[contest][user_name] = points
    else:
        if points > contests_info[contest][user_name]:
            contests_info[contest][user_name] = points

    command = input()

for contest, users in contests_info.items():
    for user_name, points in users.items():
        if user_name not in users_info:
            users_info[user_name] = points
        else:
            users_info[user_name] += points

for contest, users in contests_info.items():
    print(f"{contest}: {len(users)} participants")
    count = 1
    for user_name, points in dict(sorted(users.items(), key=lambda kvp: (-kvp[1], kvp[0]))).items():
        print(f"{count}. {user_name} <::> {points}")
        count += 1

print("Individual standings:")

count_users = 1
for username, points in sorted(users_info.items(), key=lambda kvp: (-kvp[1], kvp[0])):
    print(f"{count_users}. {username} -> {points}")
    count_users += 1

