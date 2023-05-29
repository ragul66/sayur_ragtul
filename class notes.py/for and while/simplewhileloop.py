######## Problem 1 ###############
#Write a program that prints out a diamond shape using $.
#After printing each line, wait for user input. If the user presses space, continue
#If the users presses any other key, stop printing. Maximum 10 lines
"""
def print_diamond(lines):
    for i in range(lines):
        print(' ' * (lines - i - 1) + '$' * (2 * i + 1))
        user_input = input()
        if user_input != ' ':
            break

print_diamond(10)
"""
######## Problem 2 ###############
# Computer will guess a random number. 
# user has to guess that number. for each guess, print 'High' or 'Low'
# eg - computer number - 189
# user guess 56 - print low
# user guess 678 - print high
# Get user input and print 'high' or 'low' until the user guesses the number correctly 
# https://www.w3schools.com/python/ref_random_randint.asp - read this to learn how to create a random number
"""
import random

computerNo = random.randint(3, 9)

attempt = 0
while True:
    userNo = int(input("Guess the number: "))
    if userNo < computerNo:
        print("Low")
    elif userNo > computerNo:
        print("High")
    else:
        print("Congratulations! You guessed the number correctly.")
        break
    attempt += 1

print("User guessed the number in", attempt, "attempts")
"""

"""
Example
Guess the number: 3
Low
Guess the number: 6
High
Guess the number: 5
High
Guess the number: 6
High
Guess the number: 9
High
Guess the number: 3
Low
Guess the number: 5
High
"""
########## Problem 3 ############
#Write a program for a bag shop. Shop has 100 red bags (each Rs 1000) and 200 white bags (each Rs 1500)
#Customers can buy one or more bags at a time.
#The program ends when the sales reached Rs10000 or at least 10 bags are sold. 
#Display total sales and total number of bags sold
"""
# Initialize variables
redBags, whiteBags = 100, 200
redBagPrice, whiteBagPrice = 1000, 1500
totalSales, totalBagsSold = 0, 0

while totalSales < 10000 and totalBagsSold < 10:
    # Ask customer for input
    color = input("Enter the color of the bag (red/white): ")
    quantity = int(input("Enter the quantity of bags: "))

    # Check if the requested quantity is available
    if color.lower() == "red" and quantity <= redBags:
        redBags -= quantity
        totalSales += quantity * redBagPrice
        totalBagsSold += quantity
    elif color.lower() == "white" and quantity <= whiteBags:
        whiteBags -= quantity
        totalSales += quantity * whiteBagPrice
        totalBagsSold += quantity
    else:
        print("Requested quantity is not available.")

print("Total sales: Rs", totalSales)
print("Total bags sold:", totalBagsSold)

"""