x = input()

max_num = int(''.join(sorted(str(x))[::-1]))
print(max_num)


# # .join() with lists
# numList = ['1', '2', '3', '4']
# separator = ', '
# print(separator.join(numList))
# output = 1, 2, 3, 4