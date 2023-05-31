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

def print_pattern(n):
    for i in range(2 * n - 1):
        for j in range(2 * n - 1):
            # Calculate the value at each position
            value = n - min(i, j, 2 * n - 2 - i, 2 * n - 2 - j)
            print(value, end=" ")
        print()

# Example usage
input_value = 5
print_pattern(input_value)

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

