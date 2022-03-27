import sys

int_lst = [int(x) for x in input().split()]
command = input().split()

while not command[0] == "end":
    action = command[0]
    index = command[1]

    if action == "exchange":
        index = int(index)
        if index < 0 or index > len(int_lst):
            print("Invalid index")
        else:
            int_lst = int_lst[index + 1:] + int_lst[:index + 1]

    elif action == "max" or action == "min":
        max_num = -sys.maxsize
        min_num = sys.maxsize
        if action == "max" and index == "even":
            for num in int_lst:
                if num > max_num and num % 2 == 0:
                    max_num = num
        elif action == "max" and index == "odd":
            for num in int_lst:
                if num > max_num and num % 2 != 0:
                    max_num = num
        elif action == "min" and index == "even":
            for num in int_lst:
                if num < min_num and num % 2 == 0:
                    min_num = num
        elif action == "min" and index == "odd":
            for num in int_lst:
                if num < min_num and num % 2 != 0:
                    min_num = num
        if min_num in int_lst:
            print(len(int_lst) - 1 - int_lst[::-1].index(min_num))
        elif max_num in int_lst:
            print((len(int_lst) - 1 - int_lst[::-1].index(max_num)))
        else:
            print("No matches")

    elif action == "first":
        count = int(index)
        even_odd = command[2]
        if count > len(int_lst):
            print("Invalid count")
        else:
            if even_odd == "even":
                even_lst = [x for x in int_lst if x % 2 == 0]
                print(even_lst[:count])

            elif even_odd == "odd":
                odd_lst = [x for x in int_lst if x % 2 != 0]
                print(odd_lst[:count])

    elif action == "last":
        count = int(index)
        even_odd = command[2]
        if count > len(int_lst):
            print("Invalid count")
        else:
            if even_odd == "even":
                even_lst = [x for x in int_lst if x % 2 == 0]
                if len(even_lst) < count:
                    print(even_lst)
                else:
                    print(even_lst[-count:])

            elif even_odd == "odd":
                odd_lst = [x for x in int_lst if x % 2 != 0]
                if len(odd_lst) < count:
                    print(odd_lst)
                else:
                    print(odd_lst[-count:])
    command = input().split()

print(int_lst)