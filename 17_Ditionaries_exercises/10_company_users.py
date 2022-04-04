# Write a program that keeps the information about companies and their employees.
# You will be receiving company names and an employees' id until you receive the command "End" command. Add each
# employee to the given company. Keep in mind that a company cannot have two employees with the same id.
# Print the company name and each employee's id in the following format:
# "{company_name}
# -- {id1}
# -- {id2}
# …
# -- {idN}"
# Input / Constraints
# •	Until you receive the "End" command, you will be receiving input in the format:
# "{company_name} -> {employee_id}".
# •	The input always will be valid.

companies = {}

command = input()

while not command == 'End':
    current_company = command.split(' -> ')
    company_name = current_company[0]
    employee_id = current_company[1]

    if company_name not in companies:
        companies[company_name] = []
    if employee_id not in companies[company_name]:
        companies[company_name].append(employee_id)

    command = input()


for company_name in companies.keys():
    employees = companies.get(company_name)

    print(f"{company_name}")
    students_in_course = [f"-- {name}" for name in employees]
    print(*students_in_course, sep='\n')


