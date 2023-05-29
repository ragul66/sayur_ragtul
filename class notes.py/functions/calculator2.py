#Fill in the missing code whereever it says #FillinMissingCode
#Fix the syntax errors as needed.

#This is code has functions for basic arithmetic operations. Add, subtract, multiply and divide
#The main function adds all student marks and finds the average

def addTwoNumbers(n1, n2):
    ans = n1 + n2
    return ans
def subtractAfromB(a, b):
    ans=b-a#FillinMissingCode
    return ans#FillinMissingCode

def multiplyTwoNumbers(n1,n2):
    ans=n1*n2#FillinMissingCode
    return ans#FillinMissingCode


def divideAFromB(a,b):#FillinMissingCode):
    ans=b/a 
    return ans#FillinMissingCode

#main code


 
marksInMaths = [56,78,56,45,90]
avgMaths=sum(marksInMaths)/len(marksInMaths)#FillinMissingCode to calculate avg for Maths

marksInScience = [90,78,67,8,98]
avgScience=sum(marksInScience)/len(marksInMaths)#FillinMissingCode to calculate avg for Maths


marksInHistory = [87,44,56,34,90]
avgHistory=sum(marksInHistory)/len(marksInHistory)#FillinMissingCode to calculate avg for History

avg = divideAFromB(3, addTwoNumbers(addTwoNumbers(avgMaths, avgScience), avgHistory))
#Call divide function to get the average from all three subjects
#FillinMissingCode

print("The avg mark is ", avg)

"""
Example
The avg mark is  65.13333333333333
"""