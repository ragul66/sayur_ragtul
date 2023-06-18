'''
Program 1 - Write a program to print the following pattern.
Input is 5 for the following pattern.
5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 5
5 4 3 3 3 3 3 4 5
5 4 3 2 2 2 3 4 5
5 4 3 2 1 2 3 4 5
5 4 3 2 2 2 3 4 5
5 4 3 3 3 3 3 4 5
5 4 4 4 4 4 4 4 5
5 5 5 5 5 5 5 5 5
'''

# def print_pattern(n):
#     for i in range(2 * n - 1):
#         for j in range(2 * n - 1):
#             # Calculate the value at each position
#             value = n - min(i, j, 2 * n - 2 - i, 2 * n - 2 - j)
#             print(value, end=" ")
#         print()

# # Example usage
# input_value = 5
# print_pattern(input_value)

"""
Example
5 5 5 5 5 5 5 5 5 
5 4 4 4 4 4 4 4 5 
5 4 3 3 3 3 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 2 1 2 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 3 3 3 3 4 5 
5 4 4 4 4 4 4 4 5 
5 5 5 5 5 5 5 5 5
"""
"""
Problem 2:
Get the list of employee names from the user.
Get the monthly phone sales for each employee for the first 4 months of the year.
Sort the employees by name in alphabetical order and for each employee sort their phones sales in 
ascending order.

Eg - Sam, Adam, Sara
Sam's sales - 300, 567,234,1000
Adam's Sales - 340, 456,456,234
Sara' Sales - 1000,234,3000,2000

Output sample
Adam - 456,456,340,234
Sam - ...
Sara - ...
"""
"""
# Get the number of employees from the user
num_employees = int(input("Enter the number of employees: "))

# Create empty lists to store employee names and sales
employee_names = []
employee_sales = []

# Get employee names and sales from the user
for i in range(num_employees):
    name = input("Enter employee name: ")
    sales = []
    for j in range(4):
        month_sales = int(input(f"Enter {name}'s sales for month {j+1}: "))
        sales.append(month_sales)
    employee_names.append(name)
    employee_sales.append(sales)

# Sort employee names in alphabetical order
sorted_names = sorted(employee_names)

# Print sorted employee names and their sales in descending order
for name in sorted_names:
    # Find the index of the employee in the original list
    index = employee_names.index(name)
    
    # Sort the sales for the employee in descending order
    sorted_sales = sorted(employee_sales[index], reverse=True)
    
    # Print the employee name and sorted sales
    print(f"{name} - {', '.join(map(str, sorted_sales))}")
"""
"""
Enter the number of employees: 4
Enter employee name: Ram
Enter Ram's sales for month 1: 576
Enter Ram's sales for month 2: 345
Enter Ram's sales for month 3: 678
Enter Ram's sales for month 4: 234
Enter employee name: Siva
Enter Siva's sales for month 1: 645
Enter Siva's sales for month 2: 98
Enter Siva's sales for month 3: 675
Enter Siva's sales for month 4: 984
Enter employee name: Arun
Enter Arun's sales for month 1: 847
Enter Arun's sales for month 2: 745
Enter Arun's sales for month 3: 895
Enter Arun's sales for month 4: 923
Enter employee name: Ragul
Enter Ragul's sales for month 1: 457 
Enter Ragul's sales for month 2: 476
Enter Ragul's sales for month 3: 984
Enter Ragul's sales for month 4: 284 
Arun - 923, 895, 847, 745
Ragul - 984, 476, 457, 284
Ram - 678, 576, 345, 234
Siva - 984, 675, 645, 98

"""


'''
problem 3:
Same details as above.
create a file and input the following data.
But the input is in a file in the following format

Name/Month  Sam    Adam     Sara
Month1      300     340     1000
Month2      567     456     234
Month3      234     456     3000
Month4      1000    234     2000   

Find the name of the employee who had the most the phone sales each month and add it to the end of the
table and write it back to the file

eg
Name/Month  Sam    Adam     Sara    MostSales
Month1      300     340     1000    Sara    
Month2      567     456     234     Sam    
Month3      234     456     3000    Sara
Month4      1000    234     2000    Sara


Also , print the employee who sold most phones in all 4 months added.

'''

def create_sales_data():
    
    


# Read the data from the file
with open('sales_data.txt', 'r') as file:
    lines = file.readlines()

# Parse the data into a list of lists
data = [line.strip().split() for line in lines]

# Determine the number of employees
num_employees = len(data[0]) - 1

# Iterate over each month and find the employee with the most sales
for i in range(1, len(data)):
    max_sales = -1
    max_employee = ""
    
    # Find the employee with the most sales for the current month
    for j in range(1, num_employees + 1):
        sales = int(data[i][j])
        
        if sales > max_sales:
            max_sales = sales
            max_employee = data[0][j]
    
    # Add the employee with the most sales to the end of the current month's data
    data[i].append(max_employee)

# Determine the employee with the most sales overall
overall_max_sales = -1
overall_max_employee = ""

# Find the employee with the most sales across all months
for j in range(1, num_employees + 1):
    total_sales = sum(int(data[i][j]) for i in range(1, len(data)))
    
    if total_sales > overall_max_sales:
        overall_max_sales = total_sales
        overall_max_employee = data[0][j]

# Add the "MostSales" header to the first row of the data
data[0].append("MostSales")




# Write the updated data back to the file
with open('sales_data.txt', 'w') as file:
    for row in data:
        file.write('\t'.join(row) + '\n')

file_name='sales_data.txt'
create_sales_data()


# Print the employee with the most sales overall
print("Employee with the most sales overall:", overall_max_employee)







