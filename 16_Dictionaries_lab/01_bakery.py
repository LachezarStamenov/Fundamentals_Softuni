# You will receive a single line containing some food (keys) and quantities (values). They will be separated by
# a single space (the first element is the key, the second – the value, and so on). Create a dictionary with all
# the keys and values and print it on the console.
# input = bread 10 butter 4 sugar 9 jam 12

text_as_list = input().split()

bakery = {}

for i in range(0, len(text_as_list), 2):
    key = text_as_list[i]
    value = text_as_list[i+1]
    bakery[key] = int(value)
print(bakery)