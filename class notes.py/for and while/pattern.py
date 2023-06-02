#Write code for drawing these patterns.
#Get width and length from the user.
# draw a empty rectangle woth char *
#eg 
'''
Row 5, col 7
* * * * * * *
*           *
*           *
*           *
* * * * * * *

'''
# next pattern is - empty diamond

'''
def draw_rectangle(width, length):
    for row in range(length):
        for col in range(width):
            if row == 0 or row == length - 1 or col == 0 or col == width - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

# Get width and length from the user
width = int(input("Enter the width of the rectangle: "))
length = int(input("Enter the length of the rectangle: "))

# Draw the rectangle
draw_rectangle(width, length)
'''


"""
Example
Enter the width of the rectangle: 7
Enter the length of the rectangle: 5
* * * * * * * 
*           * 
*           * 
*           * 
* * * * * * * 
"""


#next pattern is empty diamond..



def print_diamond(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")
        for j in range(2 * i + 1):
            if j == 0 or j == 2 * i:
                print("*", end="")
            else:
                print(" ", end="")
        print()
    for i in range(n - 2, -1, -1):
        for j in range(n - i - 1):
            print(" ", end="")
        for j in range(2 * i + 1):
            if j == 0 or j == 2 * i:
                print("*", end="")
            else:
                print(" ", end="")
        print()

n = int(input("Enter the size of the diamond: "))
print_diamond(n)
