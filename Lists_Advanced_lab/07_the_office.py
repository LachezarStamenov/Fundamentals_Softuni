employees_happiness = [int(el) for el in input().split()]
happiness_factor = int(input())

# employees = list((map(lambda x: int(x) * happiness_factor, employees_happiness)))
employees = [num * happiness_factor for num in employees_happiness]

list_with_happy_employees = list(filter(lambda x: x >= (sum(employees)) / len(employees), employees))

if len(list_with_happy_employees) >= len(employees)/2:
    print(f"Score: {len(list_with_happy_employees)}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {len(list_with_happy_employees)}/{len(employees)}. Employees are not happy!")
