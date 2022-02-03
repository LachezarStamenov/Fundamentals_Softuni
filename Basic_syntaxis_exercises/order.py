num_of_orders = int(input())
total_price = 0
for order in range(num_of_orders):
    coffee_price = 0
    capsule_price = float(input())
    days = int(input())
    capsules_count = int(input())
    # for day in range(1, days):
    coffee_price = capsule_price * capsules_count * days
    total_price += coffee_price
    print(f"The price for the coffee is: ${coffee_price:.2f}")
print(f"Total: ${total_price:.2f}")
