numbers = input().split() # четем от конзолата string и го превръщаме в лист
string = input() # четем string от конзолата
message = [] # създаваме празен лист, където ще записваме премахнатите символи

for i in numbers: # цикъл за обхождане на елементите в листа
    index = 0
    for num in i: # цикъл за обхождане на елементите на елемента в листа
        index += int(num)
    if len(string) < index: # проверяваме дали дължината на стринга е по-малка от индекса
        index -= len(string)

    message.append(string[index])
    string = string[:index] + string[index+1:] # намаляваме дължината на стринга с вече извадените character

print(''.join(message))
