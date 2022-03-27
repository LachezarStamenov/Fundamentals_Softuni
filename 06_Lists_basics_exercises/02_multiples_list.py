# factor = int(input())
# count = int(input())
#
# num_range = range(factor, (count * factor + 1), factor)
# lst = list(num_range)
# print(lst)

factor = int(input())
count = int(input())

lst = [int(x) for x in range(factor, count * factor + 1, factor)]
print(lst)