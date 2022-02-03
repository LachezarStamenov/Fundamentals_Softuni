circle = input().split(' ')
killed_people = int(input())
result = []
counter = 0

index = 0
while len(circle) > 0:
    counter += 1

    if counter % killed_people == 0:
        result.append(circle.pop(index))
    else:
        index += 1

    if index >= len(circle):
        index = 0

print(str(result).replace(' ', '').replace('\'', ''))

# def josephus(lst, к):
#     skip = к - 1
#     index = skip
#     dead_list = []
#     while True:
#         if index >= len(lst):
#             index = index % len(lst)
#         dead_list.append(lst.pop(index))  # kill prisoner at index
#         if len(lst) > 0:
#             index = (index + skip) % len(lst)
#         else:
#             break
#     return dead_list
#
#
# people = input().split()
# number_k = int(input())
# print(f"[{','.join(josephus(people, number_k))}]")

