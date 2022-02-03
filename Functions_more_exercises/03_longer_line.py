import math


def is_points_closer_to_zero(x1, y1, x2, y2):
    points = [(x1, y1), (x2, y2)]
    target = (0, 0)

    min_points = min(points, key=lambda point: math.hypot(target[0] - point[0], int(target[1] - point[1])))
    return math.floor(min_points[0]), math.floor(min_points[1])


def get_longest_line(x1, y1, x2, y2, x3, y3, x4, y4):
    first_line_len = 0
    first_line_len = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    second_line_len = math.sqrt((x4 - x3) ** 2 + (y4 - y3) ** 2)
    if first_line_len >= second_line_len:
        if is_points_closer_to_zero(x1, y1, x2, y2) == (x2, y2):
            print(f"({math.floor(x2)}, {math.floor(y2)})({math.floor(x1)}, {math.floor(y1)})")
        else:
            print(f"({math.floor(x1)}, {math.floor(y1)})({math.floor(x2)}, {math.floor(y2)})")
    else:
        if is_points_closer_to_zero(x3, y3, x4, y4) == (x3, y3):
            print(f"({math.floor(x3)}, {math.floor(y3)})({math.floor(x4)}, {math.floor(y4)})")
        else:
            print(f"({math.floor(x4)}, {math.floor(y4)})({math.floor(x3)}, {math.floor(y3)})")



x1_input = float(input())
y1_input = float(input())
x2_input = float(input())
y2_input = float(input())
x3_input = float(input())
y3_input = float(input())
x4_input = float(input())
y4_input = float(input())

get_longest_line(x1_input, y1_input, x2_input, y2_input, x3_input, y3_input, x4_input, y4_input)


#
# import math
#
#
# def coordination_line(lst):
#     x1,y1,x2,y2 = map(float, lst)
#     diagonal = math.sqrt(pow(x2-x1, 2) + pow(y2-y1, 2))
#     return diagonal
#
#
# def coordination_point(lst):
#     x1,y1,x2,y2 = map(float, lst)
#     first_point_to_o = math.sqrt(x1 ** 2 + y1 ** 2)
#     second_point_to_o = math.sqrt(x2 ** 2 + y2 ** 2)
#     if first_point_to_o <= second_point_to_o:
#         return print(f"({math.floor(x1)}, {math.floor(y1)})({math.floor(x2)}, {math.floor(y2)})")
#     else:
#         return print(f"({math.floor(x2)}, {math.floor(y2)})({math.floor(x1)}, {math.floor(y1)})")
#
#
# coordinates = [input() for x in range(8)]
# first_line = coordinates[:4]
# second_line = coordinates[4:]
#
# if coordination_line(first_line) >= coordination_line(second_line):
#     coordination_point(first_line)
# else:
#     coordination_point(second_line)