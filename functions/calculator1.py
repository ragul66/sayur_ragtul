#Fill in the missing code whereever it says #FillinMissingCode
#Fix the syntax errors as needed.

#This is code has functions for basic arithmetic operations. Add, subtract, multiply and divide
#The main function adds all student marks and finds the average

def addTwoNumbers(n1, n2):
    ans = n1 + n2
    return ans
def subtractAfromB(a, b):
    ans=b-a
    return ans

def multiplyTwoNumbers(n1,n2):
    ans=n1*n2
    return ans#FillinMissingCode
def divideAFromB(a, b):
    ans = b / a
    return ans #FillinMissingCode

#main code

#Get 5 marks from student and find the total
total = 0
for i in range(0,5):
    mark = int(input("Enter mark " + str(i+1) + ": ")) #correct te syntax as needed
    total=addTwoNumbers(total,mark)#FillinMissingCode


#Call divide function to get the average
avg=divideAFromB(5,total)#FillinMissingCode


print("The avg mark is ", avg)
"""
Example
Enter mark 1: 90
Enter mark 2: 89
Enter mark 3: 45
Enter mark 4: 34
Enter mark 5: 23
The avg mark is  56.2
"""