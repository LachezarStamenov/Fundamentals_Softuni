days = int(input())
daily_plunder = int(input())
expected_plunder = int(input())
total_plunder = 0

for day in range(1, days+1):
    total_plunder += daily_plunder
    if day % 3 == 0:
        total_plunder += 0.5 * daily_plunder
    if day % 5 == 0:
        total_plunder = total_plunder - (total_plunder * 0.3)
if expected_plunder != 0:
    percent_collected = (total_plunder / expected_plunder) * 100
    if total_plunder >= expected_plunder:
        print(f"Ahoy! {total_plunder:.2f} plunder gained.")
    else:
        print(f"Collected only {percent_collected:.2f}% of the plunder.")