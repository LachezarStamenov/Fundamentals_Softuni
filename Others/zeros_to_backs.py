string = input()
lst = string.split(', ')
int_list = list(map(int, lst))
temp = []
zeros = []

for index in int_list:
    if index != 0:
        temp.append(index)
    else:
        zeros.append(index)
print(temp + zeros)
