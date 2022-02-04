command = input()
total_price_without_taxes = 0
taxes = 0
total_price = 0

while not command == "special" and not command == "regular":
    current_price = float(command)
    if current_price < 0:
        print("Invalid price!")
    else:
        total_price_without_taxes += current_price

    command = input()
taxes = total_price_without_taxes * 0.2
total_price = total_price_without_taxes + taxes
if command == "special":
    total_price *= 0.9

if total_price == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price_without_taxes:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")
