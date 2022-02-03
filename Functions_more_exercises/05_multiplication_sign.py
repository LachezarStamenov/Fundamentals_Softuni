def is_positive_or_negative(n1, n2, n3):
    list_number = [n1, n2, n3]
    negative_count = 0
    positive_count = 0
    zero_count = 0

    for el in list_number:

        if int(el) < 0:
            negative_count += 1
        elif int(el) == 0:
            zero_count += 1
        else:
            positive_count += 1
    if negative_count % 2 != 0:
        print("negative")
    elif zero_count > 0:
        print("zero")
    else:
        print("positive")


first_num = int(input())
second_num = int(input())
third_num = int(input())

is_positive_or_negative(first_num, second_num, third_num)
