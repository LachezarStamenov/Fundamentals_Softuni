string_players = input().split(" ")
list_one = []
for i in string_players:
    list_one.append(i)
team_one = 11
team_two = 11
terminated = False
new_list = list(set(list_one))
for i in range(1, 11 + 1):
    team_one -= int(new_list.count(f"A-{i}"))
    team_two -= int(new_list.count(f"B-{i}"))
    if team_one < 7 or team_two < 7:
        print(f"Team A - {team_one}; Team B - {team_two}")
        print("Game was terminated")
        terminated = True
        break
if terminated != True:
    print(f"Team A - {team_one}; Team B - {team_two}")


# string_players = input().split(" ")
# list_one = []
# for i in string_players:
#     list_one.append(i)
# team_one = 11
# team_two = 11
# terminated = False
# new_list = list(set(list_one))
# for i in range(1, 11 + 1):
#     team_one -= int(new_list.count(f"A-{i}"))
#     team_two -= int(new_list.count(f"B-{i}"))
#     if team_one < 7 or team_two < 7:
#         print(f"Team A - {team_one}; Team B - {team_two}")
#         print("Game was terminated")
#         terminated = True
#         break
# if terminated != True:
#     print(f"Team A - {team_one}; Team B - {team_two}")