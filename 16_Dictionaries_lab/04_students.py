# You will be receiving names of students, their ID, and a course of programming they have taken in the format
# "{name}:{ID}:{course}".
# On the last line, you will receive a name of a course in snake case lowercase letters.
# You should print only the information of the students who have taken the corresponding course in the format: "{name} -
# {ID}" on separate lines.
# Peter:123:programming basics
# John:5622:fundamentals
# Maya:89:fundamentals
# Lilly:633:fundamentals
# fundamentals

courses = {}
while True:
    input_data = input().split(':')
    if len(input_data) == 1:
        course = input_data[0]
        break
    else:
        name = input_data[0]
        id = input_data[1]
        course = '_'.join(input_data[2].split(' '))

        if course not in courses:
            courses[course] = []
        courses[course].append(f"{name} - {id}")

output_list = courses[course]
print(*output_list, sep='\n')

# text = input()
# courses = dict()
#
# while ":" in text:
#
#     (name, id, course) = text.split(":")
#
#     if course not in courses.keys():
#         courses[course] = dict()
#
#     courses[course][id] = name
#
#     text = input()
#
# text = text.replace("_", " ")
#
# if text in courses.keys():
#     for id in courses[text]:
#         print(f"{courses[text][id]} - {id}")

