# You will be receiving key-value pairs on separate lines separated by ": " until you receive the command "statistics".
# Sometimes you may receive a product more than once. In that case, you have to add the new quantity to the existing
# one.
# When you receive the "statistics" command, print the following:
# "Products in stock:
# - {product1}: {quantity1}
# - {product2}: {quantity2}
# …
# - {productN}: {quantityN}
# Total Products: {count_all_products}
# Total Quantity: {sum_all_quantities}"

# input = bread: 4
# cheese: 2
# ham: 1
# bread: 1
# statistics

command = input()
stock = {}

while not command == "statistics":
    key, value = command.split(":")
    if key not in stock:
        stock[key] = 0
    stock[key] += int(value)

    command = input()

print("Products in stock:")
for key, value in stock.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(stock.keys())}")
print(f"Total Quantity: {sum(stock.values())}")
