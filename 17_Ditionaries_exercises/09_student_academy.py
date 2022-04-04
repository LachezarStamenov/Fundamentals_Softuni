# Write a program that keeps the information about students and their grades.
# On the first line, you will receive an integer number representing the next pair of rows. On the next lines, you
# will be receiving each student's name and their grade.
# Keep track of all grades for each student and keep only the students with an average grade higher than or equal to
# 4.50.
# Print the final dictionary with students and their average grade in the following format:
# "{name} -> {averageGrade}"
# Format the average grade to the 2nd decimal place.


n = int(input())

average_grade = 4.5
student_info = {}

for student in range(n):
    name = input()
    grade = float(input())

    if name not in student_info:
        student_info[name] = []
    student_info[name].append(grade)

for (name, grade) in student_info.items():
    student_avg_grade = sum(grade)/len(grade)
    if student_avg_grade >= average_grade:
        print(f"{name} -> {student_avg_grade:.2f}")