food_amount = float(input()) * 1000
hay_amount = float(input()) * 1000
cover_amount = float(input()) * 1000
guineas_weight = float(input()) * 1000
days = 30
daily_rate = 300
for day in range(1, days+1):

    food_amount -= daily_rate
    # every second day we reduced the hay with 5% from the rest of food_amount
    if day % 2 == 0:
        hay_amount -= food_amount * 0.05
    # every third day we reduced the cover amount with 1/3 from its weight
    if day % 3 == 0:
        cover_amount -= guineas_weight / 3
if food_amount > 0 and hay_amount > 0 and cover_amount > 0:
    print(f"Everything is fine! Puppy is happy! Food: {food_amount / 1000:.2f}, Hay: {hay_amount / 1000:.2f}, Cover: {cover_amount / 1000:.2f}.")
else:
    print('Merry must go to the pet store!')
