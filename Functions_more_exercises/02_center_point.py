import math


def print_points_closest_to_zero_coordinates(x1, y1, x2, y2):
    points = [(x1, y1), (x2, y2)]
    target = (0, 0)

    min_points = min(points, key=lambda point: math.hypot(target[0] - point[0], int(target[1] - point[1])))
    return (math.floor(min_points[0]), math.floor(min_points[1]))

x1_input = float(input())
y1_input = float(input())
x2_input = float(input())
y2_input = float(input())
print(print_points_closest_to_zero_coordinates(x1_input, y1_input, x2_input, y2_input))
