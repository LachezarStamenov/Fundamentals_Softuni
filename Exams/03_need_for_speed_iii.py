# On the first line of the standard input, you will receive an integer n – the number of cars that you can obtain.
# On the next n lines, the cars themselves will follow with their mileage and fuel available, separated by "|" in the
# following format:
# "{car}|{mileage}|{fuel}"
# Then, you will be receiving different commands, each on a new line, separated by " : ", until the "Stop" command is
# given:
# •	"Drive : {car} : {distance} : {fuel}":
# o	You need to drive the given distance, and you will need the given fuel to do that.
# If the car doesn't have enough fuel, print: "Not enough fuel to make that ride"
# o	If the car has the required fuel available in the tank, increase its mileage with the given distance, decrease its
# fuel with the given fuel, and print:
# "{car} driven for {distance} kilometers. {fuel} liters of fuel consumed."
# o	You like driving new cars only, so if a car's mileage reaches 100 000 km, remove it from the collection(s) and
# print: "Time to sell the {car}!"
# •	"Refuel : {car} : {fuel}":
# o	Refill the tank of your car.
# o	Each tank can hold a maximum of 75 liters of fuel, so if the given amount of fuel is more than you can fit in the
# tank, take only what is required to fill it up.
# o	Print a message in the following format: "{car} refueled with {fuel} liters"
# •	"Revert : {car} : {kilometers}":
# o	Decrease the mileage of the given car with the given kilometers and print the kilometers you have decreased it with
# in the following format:
# "{car} mileage decreased by {amount reverted} kilometers"
# o	If the mileage becomes less than 10 000km after it is decreased, just set it to 10 000km and
# DO NOT print anything.
# Upon receiving the "Stop" command, you need to print all cars in your possession,
# sorted by their mileage in descending order, then by their name in ascending order, in the following format:
# "{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt."
#
# Input/Constraints
# •	The mileage and fuel of the cars will be valid, 32-bit integers, and will never be negative.
# •	The fuel and distance amounts in the commands will never be negative.
# •	The car names in the commands will always be valid cars in your possession.
#
# Output
# •	All the output messages with the appropriate formats are described in the problem description.

num_of_cars = int(input())
car_info = {}
fuel_capacity = 75

for car in range(num_of_cars):
    car_type, mileage, fuel = input().split("|")
    car_info[car_type] = {'mileage': int(mileage), 'fuel': int(fuel)}

command = input()

while not command == "Stop":
    current_command = command.split(" : ")
    action = current_command[0]
    car_type = current_command[1]

    if action == "Drive":
        distance = int(current_command[2])
        fuel = int(current_command[3])
        if fuel > int(car_info[car_type]['fuel']):
            print("Not enough fuel to make that ride")
        else:
            car_info[car_type]['mileage'] += distance
            car_info[car_type]['fuel'] -= fuel
            print(f"{car_type} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
    if car_info[car_type]['mileage'] >= 100000:
        car_info.pop(car_type)
        print(f"Time to sell the {car_type}!")
    elif action == 'Refuel':
        fuel = int(current_command[2])
        refill = min(fuel, fuel_capacity - car_info[car_type]['fuel'])
        car_info[car_type]['fuel'] += refill
        print(f"{car_type} refueled with {refill} liters")

    elif action == 'Revert':
        km = int(current_command[2])
        current_km = car_info[car_type]['mileage']
        km_change = min(km, current_km - 10000)
        car_info[car_type]['mileage'] -= km_change
        if current_km - km >= 10000:
            print(f"{car_type} mileage decreased by {km_change} kilometers")

    command = input()

for key, value in car_info.items():
    print(f"{key} -> Mileage: {car_info[key]['mileage']} kms, Fuel in the tank: {car_info[key]['fuel']} lt.")

    #
    # def drive_car(data):
    #     car_name = data[1]
    #     distance = int(data[2])
    #     consumed = int(data[3])
    #     if cars_dict[car_name][1] < consumed:
    #         print("Not enough fuel to make that ride")
    #     else:
    #         cars_dict[car_name][0] += distance
    #         cars_dict[car_name][1] -= consumed
    #         print(f"{car_name} driven for {distance} kilometers. {consumed} liters of fuel consumed.")
    #     if cars_dict[car_name][0] >= 100000:  # COULD BE INTEGRATED IN THE ELSE ABOVE
    #         del cars_dict[car_name]
    #         print(f"Time to sell the {car_name}!")
    #
    #
    # def refuel_car(data):
    #     car_name = data[1]
    #     refuel = int(data[2])
    #     litres = 0
    #     if cars_dict[car_name][1] <= 75:  # MAYBE NEED OF AN ELSE
    #         if cars_dict[car_name][1] + refuel >= 75:
    #             litres = 75 - cars_dict[car_name][1]
    #             cars_dict[car_name][1] = 75  # TUK MOJE DA IMA GRESHKA
    #         else:  # CAN ALSO BE ONLY ELSE
    #             cars_dict[car_name][1] = cars_dict[car_name][1] + refuel
    #             litres = refuel
    #     print(f"{car_name} refueled with {litres} liters")
    #
    #
    # def revert_car(data):
    #     car_name = data[1]
    #     kilometers = int(data[2])
    #     current_km = cars_dict[car_name][0]
    #     km_changed = min(kilometers, current_km - 10000)
    #     cars_dict[car_name][0] -= km_changed
    #     if current_km - kilometers >= 10000:
    #         print(f"{car_name} mileage decreased by {km_changed} kilometers")
    #
    #
    # num_of_cars = int(input())
    # cars_dict = dict()
    #
    # for _ in range(num_of_cars):
    #     car_data = input().split("|")
    #     car_make = car_data[0]
    #     mileage = int(car_data[1])
    #     fuel = int(car_data[2])
    #
    #     cars_dict[car_make] = [mileage, fuel]
    #
    # command = input()
    #
    # while command != "Stop":
    #
    #     data = command.split(" : ")
    #
    #     if data[0] == "Drive":
    #         drive_car(data)
    #
    #     elif data[0] == "Refuel":
    #         refuel_car(data)
    #
    #     else:
    #         revert_car(data)
    #     command = input()
    #
    # for key in cars_dict:
    #     print(f"{key} -> Mileage: {cars_dict[key][0]} kms, Fuel in the tank: {cars_dict[key][1]} lt.")