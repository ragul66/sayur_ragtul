######## Problem 1 ###############
#write multiplication table like this
# 1 * 1 = 1
# 1 * 2 = 2
#etc. Get the number as input


multiplicationNumber = int(input("Enter the multiplication number: "))
noOfEntries = int(input("How many rows do you want to print: "))

for i in range(1, noOfEntries + 1):
    print(i, "*", multiplicationNumber, "=", i * multiplicationNumber)


"""
Example
Enter the multiplication number: 3
How many rows do you want to print: 5
1 * 3 = 3
2 * 3 = 6
3 * 3 = 9
4 * 3 = 12
5 * 3 = 15
"""
######## Problem 2 ###############
#Write a program that prints out the Fibonacci sequence up to a given number.
#example 1,2,3,5,8 , next number is the sum of previous two numbers.

def fibonacci_sequence(limit):
    sequence = [1, 1]  # Initialize the sequence with the first two numbers
    while sequence[-1] < limit:
        next_number = sequence[-1] + sequence[-2]  # Calculate the next number
        if next_number <= limit:
            sequence.append(next_number)  # Add the next number to the sequence
        else:
            break
    return sequence

limit = int(input("Enter a number: "))
fib_sequence = fibonacci_sequence(limit)

print("Fibonacci sequence up to", limit, ":")
for num in fib_sequence:
    print(num, end=" ")


"""
Example
Enter a number: 15
Fibonacci sequence up to 15 :
1 1 2 3 5 8 13 
"""
######## Problem 3  ###############
#Write a program that prints out a diamond shape using #.
# Hint - print(5 * "$") will print  - $$$$$
# Hint - print(5* "$ ") will print  - $ $ $ $ $
# n = int(input("Enter the number of rows: "))

#print the top triangle
# for i in range(n):
#     print(" "*(n-i-1) + "# "*(i+1)) 
#FillinMissingCode for drawing the bottom triangle



n=input("Enter a Symbol of your choice:")
rows=int(input("Enter the no. of rows you wish to execute the pattern:")) #input no. of rows
#print the pattern
for i in range(rows):
    for j in range(1,i+1):
        print(n,end=" ")
    print()


"""
Example
Enter a Symbol of your choice:#
Enter the no. of rows you wish to execute the pattern:6

# 
# # 
# # # 
# # # # 
# # # # #
"""