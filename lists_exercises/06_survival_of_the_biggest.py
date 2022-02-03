string_list = input().split()
numbers_to_remove = int(input())
list_of_integers = list(map(int, string_list))

for number in range(numbers_to_remove):
    list_of_integers.remove(min(list_of_integers))

print(", ".join(str(list_of_integers) for list_of_integers in list_of_integers))


# print(*list_of_integers, sep=', ')

#     list_to_string = [str(int) for int in list_of_integers]
# print(", ".join(list_to_string))





