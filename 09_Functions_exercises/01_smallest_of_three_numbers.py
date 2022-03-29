def get_smallest_num_from_three_nums(num1, num2, num3):
    if num1 < num2 and num1 < num3:
        return num1
    elif num2 < num1 and num2 < num3:
        return num2

    return num3


num1 = int(input())
num2 = int(input())
num3 = int(input())

result = get_smallest_num_from_three_nums(num1, num2, num3)
print(result)