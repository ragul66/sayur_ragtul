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

#Example 1

# Enter Marks Obtained in 5 Subjects: 
# 89
# 78
# 67
# 78
# 78
# Average mark= 78.0

#Example 2
# Enter Marks Obtained in 5 Subjects: 
# 56
# 67
# 45
# 78
# 98
# Average mark= 68.8

#using while loop
total = 0
noOfStudents = 5
i = 0
while (i < noOfStudents):
     mark=float(input("Enter the marks you got"))

     total += mark
     i += 1
print ("Avg is ",)
