############# Problem 1 ###########
#Google and find the tax slabs for income tax for India. Write a program to calculate the income tax for an 
#individual. Input is Salary. Optional input - any deductions.


income=input("Enter the Income amount")
if(income==5,00,000):
    print("Incometax=NIL")
elif(income>5,00,000 and income<=10,00,000):
    income=



############ Problem 2 ####
#Calculate the BMI and if the person is underweihgt/normal/overweight/obese
#Google how to calculate BMI and decide on the input.

########## Problem 3 ##########
##buy choc and cake
# one choc is Rs 200
# one cake is 150
#get budget from user. Also get the total number of choc and cakes that the shop has
#Hint - you can buy choc/Cake only if shop has it.

#find how many choc and cake the user can buy.

############## Problem 4 ##############
#Calculate the Grade for a student, using 3 marks.
# The student has 100 marks in any one subject, Grade is A.
# if the student has 90 or above in any one subject  Grade is B
# if the student has 60 or above in any one subject  Grade is C
# if the student has 50 or less  in all subjects  Grade is F, otherwise Grade is D.

#Code
mark1 =90
mark2 =100
mark3 = 60

if(mark1 == 100 or mark2 == 100 or mark3 == 100): #at least one mark is 100
    print ("Grade A")
elif(mark1>90 or mark2>90 or mark3>90):
    print ("Grade B")
elif (mark1>60 or mark2>60 or mark3>60):
    print("Garde C")
elif(mark1<=50 and mark2<=50 and mark3<=50):
    print ("Grade F")
else:
    print ("Grade D")
