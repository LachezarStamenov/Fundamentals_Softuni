from math import ceil

num_students = int(input())
num_of_lectures = int(input())
additional_bonus = int(input())

bonus_list = []
attendance_list = []
is_broken = False

for student in range(1, num_students + 1):
    count_of_attendances_for_current_student = int(input())
    if num_of_lectures == 0 or num_students == 0:
        is_broken = True
        break
    else:
        attendance_list.append(count_of_attendances_for_current_student)
        current_total_bonus = count_of_attendances_for_current_student / num_of_lectures * (5 + additional_bonus)
        bonus_list.append(current_total_bonus)

if is_broken:
    maximum_bonus = 0
    print(f"Max Bonus: {maximum_bonus}.")
    print(f"The student has attended 0 lectures.")
else:
    maximum_bonus = max(bonus_list)
    index_of_maximum = bonus_list.index(maximum_bonus)
    print(f"Max Bonus: {ceil(maximum_bonus)}.")
    print(f"The student has attended {attendance_list[index_of_maximum]} lectures.")