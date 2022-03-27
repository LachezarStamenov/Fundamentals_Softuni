days = int(input())
num_of_players = int(input())
groups_energy = float(input())
water_per_day_per_person = float(input())
food_per_day_per_person = float(input())

total_water_amount = days * num_of_players * water_per_day_per_person
total_food_amount = days * num_of_players * food_per_day_per_person

for day in range(1, days + 1):
    energy_lose = float(input())
    groups_energy -= energy_lose
    if groups_energy <= 0:
        break

    if day % 2 == 0:
        groups_energy += groups_energy * 0.05
        total_water_amount -= total_water_amount * 0.3

    if day % 3 == 0:
        total_food_amount -= (total_food_amount / num_of_players)
        groups_energy += groups_energy * 0.1

if groups_energy > 0:
    print(f"You are ready for the quest. You will be left with - {groups_energy:.2f} energy!")
else:
    print(f"You will run out of energy. You will be left with {total_food_amount:.2f} food and {total_water_amount:.2f} water.")