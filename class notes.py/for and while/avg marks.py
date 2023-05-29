#write code for both for and while loop
#Get marks from 5  students and calculate avg
#
#for loop

mark = []
tot = 0
print("Enter Marks Obtained in 5 Subjects: ")
for i in range(5):
    mark.insert(i, int(input()))
for i in range(5):
    tot = tot + mark[i]

avg=tot/5
print("Average mark=",avg)
"""
Example 1

Enter Marks Obtained in 5 Subjects: 
89
78
67
78
78
Average mark= 78.0

Example 2
Enter Marks Obtained in 5 Subjects: 
56
67
45
78
98
Average mark= 68.8
"""

#using for loop
total = 0
noOfStudents = 5
i = 0

while i < noOfStudents:
    # Get user input
    mark = int(input("Enter the mark for student " + str(i + 1) + ": "))
    total += mark
    i += 1

average = total / noOfStudents
print("Avg is", average)

"""
Example
Enter the mark for student 1: 89
Enter the mark for student 2: 56
Enter the mark for student 3: 45
Enter the mark for student 4: 34
Enter the mark for student 5: 56
Avg is 56.0
"""