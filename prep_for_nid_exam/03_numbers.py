int_sequence = [int(num) for num in input().split()]
int_sequence.sort(reverse=True)

avg = sum(int_sequence) / len(int_sequence)

top_five_greater_nums = []

for el in int_sequence:
    if len(top_five_greater_nums) < 5:
        if el > avg:
            top_five_greater_nums.append(el)
if len(top_five_greater_nums) > 0:
    print(*top_five_greater_nums, sep=" ")
else:
    print("No")