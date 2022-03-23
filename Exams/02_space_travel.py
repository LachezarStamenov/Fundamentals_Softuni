rout = input().split("||")
fuel_amount = int(input())
ammunition_amount = int(input())

for el in rout:
    command = el.split()[0]

    if command == "Travel":
        num = int(el.split()[1])

        if fuel_amount < num:
            print(f"Mission failed.")
            break
        if fuel_amount >= num:
            fuel_amount -= num
            print(f"The spaceship travelled {num} light-years.")

    elif command == "Enemy":
        num = int(el.split()[1])
        if ammunition_amount >= num:
            ammunition_amount -= num
            print(f"An enemy with {num} armour is defeated.")
        elif ammunition_amount < num and fuel_amount > num * 2:
            fuel_amount -= num * 2
            print(f"An enemy with {num} armour is outmaneuvered.")
        else:
            print(f"Mission failed.")
            break

    elif command == "Repair":
        num = int(el.split()[1])
        fuel_amount += num
        ammunition_amount += num * 2
        print(f"Ammunitions added: {num * 2}.")
        print(f"Fuel added: {num}.")
    elif command == "Titan":
        print(f"You have reached Titan, all passengers are safe.")
        break