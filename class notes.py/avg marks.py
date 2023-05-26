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

#using while loop
total = 0
noOfStudents = 5
i = 0
while (i < noOfStudents):
     mark=input("Enter the mark")
     total += mark[i]
i += 1
print ("Avg is ",total)

