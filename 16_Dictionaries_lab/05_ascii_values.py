# Write a program that receives a list of characters separated by ", ". It should create a dictionary with each
# character as a key and its ASCII value as a value. Try solving that problem using comprehension.
#input = a, b, c, a

string_as_list = input().split(", ")
char_dict = {word: ord(word) for word in string_as_list}
print(char_dict)


