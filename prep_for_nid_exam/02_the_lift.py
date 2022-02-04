number_of_people = int(input())

current_state_lift = [int(cart) for cart in input().split(" ")]

for i in range(len(current_state_lift)):
    can_load = min(4 - current_state_lift[i], number_of_people)
    current_state_lift[i] += can_load
    number_of_people -= can_load

if number_of_people > 0:
    print(f"There isn't enough space! {number_of_people} people in a queue!")
elif len([cart for cart in current_state_lift if cart < 4]) > 0:
    print("The lift has empty spots!")

print(" ".join([str(cart) for cart in current_state_lift]))
