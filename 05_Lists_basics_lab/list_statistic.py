first_num = int(input())

positive_lst = []
negative_lst = []
positive_count = 0
negative_sum = 0

for i in range(first_num):
    current_num = int(input())
    if current_num > 0:
        positive_count += 1
        positive_lst.append(current_num)
    elif current_num < 0:
        negative_sum += current_num
        negative_lst.append(current_num)
print(positive_lst)
print(negative_lst)
print(f"Count of positives: {positive_count}")
print(f"Sum of negatives: {negative_sum}")