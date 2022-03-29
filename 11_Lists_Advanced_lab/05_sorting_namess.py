string = input().split(", ")
sorted_list = sorted(string, key=lambda  x: (-len(x), x)) # Use a sorted() function to sort the names by their length first, and then - alphabetically
print(sorted_list)