n = int(input())

evens = []
odds = []
positive = []
negative = []

for _ in range(n):
    current_number = int(input())

    if current_number % 2 == 0:
        evens.append(current_number)
    if current_number % 2 == 1:
        odds.append(current_number)
    if current_number < 0:
        negative.append(current_number)
    if current_number >= 0:
        positive.append(current_number)
command = input()

print(eval(command))
# if command == "even":
#     print(evens)
# elif command == "odd":
#     print(odds)
# elif command == "positive":
#     print(positive)
# else:
#     print(negative)
