import sys

snowballs = int(input())
max_ball_size = -sys.maxsize
max_weight = -sys.maxsize
max_quality = - sys.maxsize
max_time_needed = -sys.maxsize

for ball in range(snowballs):
    snowball_weight = int(input())
    time_needed = int(input())
    quality = int(input())
    snowball_value = (snowball_weight / time_needed) ** quality
    if snowball_value > max_ball_size:
        max_ball_size = snowball_value
        max_weight = snowball_weight
        max_time_needed = time_needed
        max_quality = quality
print(f"{max_weight} : {max_time_needed} = {max_ball_size:.0f} ({max_quality})")