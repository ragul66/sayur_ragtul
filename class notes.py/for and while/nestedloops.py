######## Problem  1 ###############
# Get and print the 2 marks each for 3 students. Also, get each studen't name
# output should be
# Mark 1 for Student 1 is 55
# Mark 2 for Student 1 is 67
# Mark 1 for Student 2 is 56 
#etc

for student in range(1, 4):
    student_name = input(f"Enter name for Student {student}: ")
    for mark in range(1, 4):
      input_mark = float(input(f"Enter Mark {mark} for Student {student}: "))
      print(f"Mark {mark} for {student_name} is {input_mark}")

"""
Example
Enter name for Student 1: ragul
Enter Mark 1 for Student 1: 34
Mark 1 for ragul is 34.0
Enter Mark 2 for Student 1: 45
Mark 2 for ragul is 45.0
Enter Mark 3 for Student 1: 34
Mark 3 for ragul is 34.0
Enter name for Student 2: gokul
Enter Mark 1 for Student 2: 65
Mark 1 for gokul is 65.0
Enter Mark 2 for Student 2: 76
Mark 2 for gokul is 76.0
Enter Mark 3 for Student 2: 89
Mark 3 for gokul is 89.0
Enter name for Student 3: vasanth
Enter Mark 1 for Student 3: 78
Mark 1 for vasanth is 78.0
Enter Mark 2 for Student 3: 90
Mark 2 for vasanth is 90.0
Enter Mark 3 for Student 3: 89
Mark 3 for vasanth is 89.0

"""

    
######### Problem 1.1
#same problem as above, but output should have the student name and all the marks in the same line.
# Eg - Input - Student Name - Chitra, Mark1 1 55, Mark 2 67
#output -  Chitra's marks 55, 67


######## Problem  2 ###############
#Print multiplication tables from 7 to 16, each number upto 12 rows.
for num in range(7, 17):
    print(f"Multiplication Table of {num}:")
    for i in range(1, 13):
        result = num * i
        print(f"{num} x {i} = {result}")
    print()


"""
Multiplication Table of 7:
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
7 x 11 = 77
7 x 12 = 84

Multiplication Table of 8:
8 x 1 = 8
8 x 2 = 16
8 x 3 = 24
8 x 4 = 32
8 x 5 = 40
8 x 6 = 48
8 x 7 = 56
8 x 8 = 64
8 x 9 = 72
8 x 10 = 80
8 x 11 = 88
8 x 12 = 96

Multiplication Table of 9:
9 x 1 = 9
9 x 2 = 18
9 x 3 = 27
9 x 4 = 36
9 x 5 = 45
9 x 6 = 54
9 x 7 = 63
9 x 8 = 72
9 x 9 = 81
9 x 10 = 90
9 x 11 = 99
9 x 12 = 108

Multiplication Table of 10:
10 x 1 = 10
10 x 2 = 20
10 x 3 = 30
10 x 4 = 40
10 x 5 = 50
10 x 6 = 60
10 x 7 = 70
10 x 8 = 80
10 x 9 = 90
10 x 10 = 100
10 x 11 = 110
10 x 12 = 120

Multiplication Table of 11:
11 x 1 = 11
11 x 2 = 22
11 x 3 = 33
11 x 4 = 44
11 x 5 = 55
11 x 6 = 66
11 x 7 = 77
11 x 8 = 88
11 x 9 = 99
11 x 10 = 110
11 x 11 = 121
11 x 12 = 132

Multiplication Table of 12:
12 x 1 = 12
12 x 2 = 24
12 x 3 = 36
12 x 4 = 48
12 x 5 = 60
12 x 6 = 72
12 x 7 = 84
12 x 8 = 96
12 x 9 = 108
12 x 10 = 120
12 x 11 = 132
12 x 12 = 144

Multiplication Table of 13:
13 x 1 = 13
13 x 2 = 26
13 x 3 = 39
13 x 4 = 52
13 x 5 = 65
13 x 6 = 78
13 x 7 = 91
13 x 8 = 104
13 x 9 = 117
13 x 10 = 130
13 x 11 = 143
13 x 12 = 156

Multiplication Table of 14:
14 x 1 = 14
14 x 2 = 28
14 x 3 = 42
14 x 4 = 56
14 x 5 = 70
14 x 6 = 84
14 x 7 = 98
14 x 8 = 112
14 x 9 = 126
14 x 10 = 140
14 x 11 = 154
14 x 12 = 168

Multiplication Table of 15:
15 x 1 = 15
15 x 2 = 30
15 x 3 = 45
15 x 4 = 60
15 x 5 = 75
15 x 6 = 90
15 x 7 = 105
15 x 8 = 120
15 x 9 = 135
15 x 10 = 150
15 x 11 = 165
15 x 12 = 180

Multiplication Table of 16:
16 x 1 = 16
16 x 2 = 32
16 x 3 = 48
16 x 4 = 64
16 x 5 = 80
16 x 6 = 96
16 x 7 = 112
16 x 8 = 128
16 x 9 = 144
16 x 10 = 160
16 x 11 = 176
16 x 12 = 192
"""

######## Problem  3 ###############
#Print Chess board (alternate black and white squares)
#print('\u25A0') - will print white Square. You can use "B" to print black squares

# Size of the chessboard
board_size = 8

# Loop through rows
for row in range(board_size):
    # Loop through columns
    for col in range(board_size):
        # Determine the square color based on row and column indices
        if (row + col) % 2 == 0:
            square_color = '\u25A0'  # White square
        else:
            square_color = 'B'  # Black square
        
        # Print the square color
        print(square_color, end=' ')
    
    # Move to the next row
    print()
"""
■ B ■ B ■ B ■ B 
B ■ B ■ B ■ B ■ 
■ B ■ B ■ B ■ B 
B ■ B ■ B ■ B ■ 
■ B ■ B ■ B ■ B 
B ■ B ■ B ■ B ■ 
■ B ■ B ■ B ■ B 
B ■ B ■ B ■ B ■
"""
######## Problem  4  ###############

#print a multiplication table like below.
#get user intput for start and end numbers. 
#the following example uses 1 to 5.

#      1  2  3  4  5
#   ********************
# 1 |  1  2  3  4  5
# 2 |  2  4  6  8 10
# 3 |  3  6  9 12 15
# 4 |  4  8 12 16 20
# 5 |  5 10 15 20 25

start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

print("    ", end="")
for i in range(start, end + 1):
    print("{:4d}".format(i), end="")
print("\n  " + "*" * (4 * (end - start + 1)))

for i in range(start, end + 1):
    print("{:2d} |".format(i), end="")
    for j in range(start, end + 1):
        print("{:4d}".format(i * j), end="")
    print()

"""
Example
       1   2   3   4   5   6   7
  ****************************
 1 |   1   2   3   4   5   6   7
 2 |   2   4   6   8  10  12  14
 3 |   3   6   9  12  15  18  21
 4 |   4   8  12  16  20  24  28
 5 |   5  10  15  20  25  30  35
 6 |   6  12  18  24  30  36  42
 7 |   7  14  21  28  35  42  49
"""