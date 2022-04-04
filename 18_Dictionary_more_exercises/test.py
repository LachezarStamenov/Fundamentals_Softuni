import colour as colour

dwarfs = {}
hat_colours = {}

input_line = input()


while not input_line == "Once upon a time":
    name = input_line.split(' <:> ')[0]
    h_color = input_line.split(' <:> ')[1]
    value = int(input_line.split(' <:> ')[2])

    if name in dwarfs:
        current_physic = max(value, dwarfs[name][h_color][value])
    else:
        dwarfs[name] = {h_color: value}

        if not colour in hat_colours:
            hat_colours[colour] = 0
        hat_colours[colour] += 1
    input_line = input()

sorted_dwarfes = sorted(dwarfs.items(), key=lambda item: (item[1], hat_colours[item[0][1]]), reverse=True)
for dwarf in sorted_dwarfes:
    print(f'({dwarf[0][1]}) {dwarf[0][0]} <-> {dwarf[1]}')