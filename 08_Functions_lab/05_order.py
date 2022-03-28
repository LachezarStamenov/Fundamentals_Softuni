def get_total_price(product, quantity):
    total_price = 0
    coffee_price = 1.5
    water_price = 1.0
    coke_price = 1.4
    snacks_price = 2.0

    if product == 'coffee':
        total_price += coffee_price * quantity
    elif product == 'water':
        total_price += water_price * quantity
    elif product == 'coke':
        total_price += coke_price * quantity
    elif product == "snacks":
        total_price += snacks_price * quantity
    return total_price


product_type = input()
quantity = int(input())
print(f"{get_total_price(product_type, quantity):.2f}")