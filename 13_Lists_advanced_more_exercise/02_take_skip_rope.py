string = input() # въвеждаме стринг от конзолата

number_list = [int(num) for num in string if num.isdigit()]   # от въведения стринг поставяме в лист всички числа
non_numbers = [num for num in string if not num.isdigit()]   # от въведения стринг поставяме в лист всички други символи

taken_list = [number_list[i] for i in range(len(number_list)) if i % 2 == 0]  # създаваме лист от четните позиции
skipped_list = [number_list[i] for i in range(len(number_list)) if i % 2 != 0]   # създаваме лист от нечетните позиции

take_number = 0
skip_number = 0

new_string = ""

for i in range(len(taken_list)):    # завъртаме цикъл в диапазон от 0 до дължината на листа на взетите
    take_number = taken_list[i]
    skip_number = skipped_list[i]
    new_string += "".join(non_numbers[:take_number])  # в нов стринг добавяме взетите chars от всяко завъртане на цикъла и ги конкатенираме
    del non_numbers[0:take_number + skip_number] # изтриваме взетите букви и пропуснатите от оригиналния лист от chars

print(new_string)


# string_name = input()
#
# number_list = []
# string_list = []
# take_list = []
# skip_list = []
# for i in range(len(string_name)):
#     if string_name[i].isdigit():
#         number_list.append(int(string_name[i]))
#     else:
#         string_list.append(string_name[i])
#
# for x in range(len(number_list)):
#     if x % 2 == 0:
#         take_list.append(number_list[x])
#     else:
#         skip_list.append(number_list[x])
#
# take_number = 0
# skip_number = 0
#
# index = 0
# new_string = ""
#
# for i in range(len(take_list)):
#     take_number = take_list[i]
#     skip_number = skip_list[i]
#     new_string += "".join(string_list[:take_number])
#     del string_list[0:take_number + skip_number]
#
# print(new_string)