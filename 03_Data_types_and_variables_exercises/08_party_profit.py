import math

group_size = int(input())
days = int(input())
coins = 0
companions_count = group_size

for day in range(1, days + 1):

    if day % 15 == 0:
        companions_count += 5
    if day % 10 == 0:
        companions_count -= 2
    coins += 50 - (companions_count * 2)
    if day % 5 == 0:
        coins += 20 * companions_count
        if day % 5 == 0 and day % 3 == 0:
            coins -= 2 * companions_count
    if day % 3 == 0:
        coins -= companions_count * 3
print(f"{companions_count} companions received {math.floor(coins / companions_count)} coins each.")