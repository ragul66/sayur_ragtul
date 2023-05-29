############# Problem 1 ###########
#Google and find the tax slabs for income tax for India. Write a program to calculate the income tax for an 
#individual. Input is Salary. Optional input - any deductions.


def calculate_income_tax(salary, deductions=0):
    taxable_income = salary - deductions

    if taxable_income <= 250000:
        tax = 0
    elif 250001 <= taxable_income <= 500000:
        tax = (taxable_income - 250000) * 0.05
    elif 500001 <= taxable_income <= 1000000:
        tax = 12500 + (taxable_income - 500000) * 0.2
    else:
        tax = 112500 + (taxable_income - 1000000) * 0.3

    return tax

salary = float(input("Enter the salary: "))
deductions = float(input("Enter the deductions (optional): "))

income_tax = calculate_income_tax(salary, deductions)
print("Income tax to be paid: ₹", income_tax)

"""
Example
Enter the salary: 1000000
Enter the deductions (optional): 20000
Income tax to be paid: ₹ 108500.0
"""

############ Problem 2 ####
#Calculate the BMI and if the person is underweihgt/normal/overweight/obese
#Google how to calculate BMI and decide on the input.

Height=float(input("Enter your height in centimetres: "))
Weight=float(input("Enter your Weight in Kg: "))
Height = Height/100
BMI=Weight/(Height*Height)
print("your Body Mass Index is: ",BMI)
if(BMI>0):
	if(BMI<=16):
		print("you are severely underweight")
	elif(BMI<=18.5):
		print("you are underweight")
	elif(BMI<=25):
		print("you are Healthy")
	elif(BMI<=30):
		print("you are overweight")
	else: print("you are severely overweight")
else:("enter valid details")

"""
Example:
Enter your height in centimetres: 167
Enter your Weight in Kg: 55
your Body Mass Index is:  19.721036967980208
you are Healthy
"""

########## Problem 3 ##########
##buy choc and cake
# one choc is Rs 200
# one cake is 150
#get budget from user. Also get the total number of choc and cakes that the shop has
#Hint - you can buy choc/Cake only if shop has it.

#find how many choc and cake the user can buy.

choc_price = 200
cake_price = 150

# Get budget from the user
budget = float(input("Enter your budget: "))

# Get the total number of chocolates and cakes available at the shop
total_choc = int(input("Enter the total number of chocolates available: "))
total_cake = int(input("Enter the total number of cakes available: "))

# Calculate the maximum number of chocolates and cakes that can be bought
max_choc = min(total_choc, int(budget / choc_price))
max_cake = min(total_cake, int(budget / cake_price))

# Display the maximum number of chocolates and cakes that can be bought
print("You can buy a maximum of", max_choc, "chocolates.")
print("You can buy a maximum of", max_cake, "cakes.")


"""
Example
Enter your budget: 1000
Enter the total number of chocolates available: 6
Enter the total number of cakes available: 7
You can buy a maximum of 5 chocolates.
You can buy a maximum of 6 cakes.
"""





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
elif(mark1>=90 or mark2>=90 or mark3>=90):
    print ("Grade B")
elif (mark1>=60 or mark2>=60 or mark3>=60):
    print("Garde C")
elif(mark1<=50 and mark2<=50 and mark3<=50):
    print ("Grade F")
else:
    print ("Grade D")

"""
Example
Grade A
"""