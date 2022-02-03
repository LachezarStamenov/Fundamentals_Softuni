list_of_integers = [1, 3, 5, 7, 9]
command = input()

count_first = 2
even_odd = "odd"


def first():
    my_list = []
    if len(list_of_integers) < count_first:
        return "Invalid count"
    else:
        if even_odd == "even":
            my_list.extend([el for el in list_of_integers if el % 2 == 0])
            return my_list[:count_first]
        elif even_odd == "odd":
            my_list.extend([el for el in list_of_integers if el % 2 == 1])
            return my_list[:count_first]


print(first())

