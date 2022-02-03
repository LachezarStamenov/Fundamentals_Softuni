# notes = [0] * 10
#
# while True:
#     command = input()
#     if command == "End":
#         break
#     current_command = command.split("-")
#     importance = int(current_command[0])-1
#     note = current_command[1]
#     notes.pop(importance)
#     notes.insert(importance, note)
#
# result = [element for element in notes if element != 0]
# print(result)

note = input()
todo_list = [0] * 10

while not note == "End":
    importance, task = note.split("-")
    importance = int(importance) - 1
    todo_list[importance] = task
    note = input()
print([task for task in todo_list if not task == 0])

