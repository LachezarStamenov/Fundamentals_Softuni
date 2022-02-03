rows_count = int(input())  # enter the number of rows
coord_list = []

for i in range(rows_count):   # loop for feed the list
    coord_list.append(input().split())

coord_lst_as_int = [[int(el) for el in sub] for sub in coord_list]   # converting "coord_list" elements in integers

attacks_list = input().split()
ships_destroyed = 0


for element in attacks_list:   # loop into the attacks list
    coord1, coord2 = element.split('-')
    coord1 = int(coord1)
    coord2 = int(coord2)
    if coord_lst_as_int[coord1][coord2] > 0:  # check if the element with the given coordinates is > 0
        coord_lst_as_int[coord1][coord2] -= 1
        if coord_lst_as_int[coord1][coord2] == 0:   # check if the element with the given coordinates is equal to 0
            ships_destroyed += 1   # if yes - destroy the ship

print(ships_destroyed)