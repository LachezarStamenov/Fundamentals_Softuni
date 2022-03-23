students = int(input())
total_lectures = int(input())
bonus = int(input())
max_bonus = 0
max_student_attendance = 0

for student in range(1, students + 1):
    count_of_attendances = int(input())
    total_bonus = count_of_attendances / total_lectures * (5 + bonus)
    if total_bonus >= max_bonus:
        max_bonus = total_bonus
        max_student_attendance = count_of_attendances
print(f"Max Bonus: {max_bonus:.0f}.")
print(f"The student has attended {max_student_attendance} lectures.")

