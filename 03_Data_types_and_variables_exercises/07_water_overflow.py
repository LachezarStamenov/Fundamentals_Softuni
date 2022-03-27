num_of_lines = int(input())
tank_capacity = 255
total_water = 0
rest_capacity = 0
for num in range(num_of_lines):
    liters_of_water = int(input())
    rest_capacity = tank_capacity - total_water
    if rest_capacity < liters_of_water:
        print(f"Insufficient capacity!")
        continue
    else:
        total_water += liters_of_water
print(total_water)