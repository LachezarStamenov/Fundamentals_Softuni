# You will be given key-value pairs of products and quantities (on a single line separated by space). On the following
# line, you will be given products to search for. Check for each product. You have 2 possibilities:
# •	If you have the product, print "We have {quantity} of {product} left".
# •	Otherwise, print "Sorry, we don't have {product}".
# input = cheese 10 bread 5 ham 10 chocolate 3
# jam cheese ham tomatoes

elements = input().split()

bakery = {}

for i in range(0, len(elements), 2):
    key = elements[i]
    value = elements[i+1]
    bakery[key] = int(value)

searched_product = input().split()

for item in searched_product:
    if item in bakery:
        print(f"We have {bakery[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")

