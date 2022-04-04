data = input()

submissions = {}
students = {}

while not " " in data:
    current_data = data.split("-")
    name = current_data[0]
    language = current_data[1]

    if language == "banned":
     del students[name]

    else:
        points = int(current_data[2])
        if name not in students:
            students[name] = points
        else:
            if students.get(name) < points:
                students[name] = points
        if language in submissions:
            submissions[language] += 1
        else:
            submissions[language] = 1

    data = input()

print("Results:")
for user, points in students.items():
    print(f"{user} | {points}")
print("Submissions:")
for submission, count in submissions.items():
    print(f"{submission} - {count}")
