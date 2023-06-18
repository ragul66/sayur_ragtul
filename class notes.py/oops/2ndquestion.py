class Employee:
    def __init__(self, name, hourly_rate):
        self.name = name
        self.hourly_rate = hourly_rate

    def calculate_salary(self, hours_worked):
        return self.hourly_rate * hours_worked

# Main program
num_employees = int(input("Enter the number of employees: "))
employee_list = []

for i in range(num_employees):
    name = input("Enter the employee name: ")
    hourly_rate = float(input("Enter the hourly rate for {}: ".format(name)))
    employee = Employee(name, hourly_rate)
    employee_list.append(employee)

max_salary = 0
employee_with_max_salary = None

for employee in employee_list:
    hours_worked = float(input("Enter the number of hours {} worked in May: ".format(employee.name)))
    salary = employee.calculate_salary(hours_worked)
    
    if salary > max_salary:
        max_salary = salary
        employee_with_max_salary = employee

print("Employee with the highest salary:")
print("Name:", employee_with_max_salary.name)
print("Salary:", max_salary)
