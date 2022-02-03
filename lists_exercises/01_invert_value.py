string = input().split(' ')
int_list = [int(element) for element in string]
converted_list = [element * -1 for element in int_list]
print(converted_list)

# print([-int(el) for el in input().split()])