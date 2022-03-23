init_array_as_lst = list(map(int, input().split()))

command = input().split()

while not command[0] == "end":

    # takes two elements and swap their places
    if command[0] == "swap":
        index1 = int(command[1])
        index2 = int(command[2])
        init_array_as_lst[index1], init_array_as_lst[index2] = init_array_as_lst[index2], init_array_as_lst[index1]

    # takes element at the 1st index and multiply it with the element at 2nd index. Result is saved on 1 index.
    elif command[0] == "multiply":
        index1 = int(command[1])
        index2 = int(command[2])
        result = init_array_as_lst[index1] * init_array_as_lst[index2]
        init_array_as_lst[index1] = result

    # decrease all elements with 1
    elif command[0] == "decrease":
        init_array_as_lst = [num - 1 for num in init_array_as_lst]
    command = input().split()

print(*init_array_as_lst, sep=", ")