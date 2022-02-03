import math

numbers = list(map(int, input().split(", ")))

max_num = max(numbers)
num_of_groups = math.ceil(max_num / 10)

for i in range(1, num_of_groups + 1):
    upper_limit = i * 10
    lower_limit = upper_limit - 10
    current_range = [n for n in numbers if lower_limit < n <= upper_limit]

    print(f"Group of {i*10}'s: {current_range} ")
