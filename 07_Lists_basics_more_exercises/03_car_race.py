cars_times_string = input().split()

left_player = []
right_player = []
num_of_players = 2
left_total_time = 0
right_total_time = 0

for player in range(num_of_players):

    half = int(len(cars_times_string)/2)
    left_player = cars_times_string[0:half]
    right_player = cars_times_string[half + 1::]

for index_player in range(len(left_player)):
    left_total_time += int(left_player[index_player])
    if int(left_player[index_player]) == 0:
        left_total_time *= 0.8
for index_player in range(len(right_player)-1, -1, -1):
    right_total_time += int(right_player[index_player])
    if int(right_player[index_player]) == 0:
        right_total_time *= 0.8
if left_total_time < right_total_time:
    print(f"The winner is left with total time: {left_total_time:.1f}")
elif left_total_time > right_total_time:
    print(f"The winner is right with total time: {right_total_time:.1f}")