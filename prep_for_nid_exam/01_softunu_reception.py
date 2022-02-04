first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
student_count = int(input())
needed_hours = 0
total_efficiency = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency

while student_count > 0:
    student_count -= total_efficiency
    needed_hours += 1
    if needed_hours % 4 == 0:
        needed_hours += 1
print(f"Time needed: {needed_hours}h.")

