# You will be given strings on separate lines until you receive an "end" command. Write a program that reverses strings
# and prints each pair on a separate line in the format "{word} = {reversed_word}".


data = input()

while not data == "end":
    reversed_text = data[::-1]
    print(data + " = " + reversed_text)

    data = input()