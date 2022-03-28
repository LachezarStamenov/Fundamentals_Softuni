def get_absolute_value(string):
    lst_of_absolute_value = []
    for num in string:
        current_num = float(num)
        lst_of_absolute_value.append(abs(current_num))
    return lst_of_absolute_value


string = input().split(' ')
result = get_absolute_value(string)
print(result)
