
dwarfs = {}
hat_colors = {}
input_line = input()


while not input_line == "Once upon a time":
    name, colour, physics = input_line.split(' <:> ')
    key = (name, colour)
    value = int(physics)

    if key in dwarfs:
        dwarfs[key] = max(value, dwarfs.get(key))
    else:
        dwarfs[key] = value

        if not colour in hat_colors:
            hat_colors[colour] = 0
        hat_colors[colour] += 1

    input_line = input()

sorted_dwarfes = sorted(dwarfs.items(), key=lambda item: (item[1], hat_colors[item[0][1]]), reverse=True)
for dwarf in sorted_dwarfes:
    print(f'({dwarf[0][1]}) {dwarf[0][0]} <-> {dwarf[1]}')



