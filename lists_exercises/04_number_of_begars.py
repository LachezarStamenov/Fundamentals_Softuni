string = input().split(", ")
count_of_beggars = int(input())
new_list = []
start_index = 0
for beggar in range(count_of_beggars):
    sum_total = 0
    for sum in range(start_index, len(string), count_of_beggars):

        sum_total += int(string[sum])
    new_list.append(sum_total)
    start_index += 1
print(new_list)
