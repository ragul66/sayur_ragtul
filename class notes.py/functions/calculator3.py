#Fix the syntax errors as needed.

#This is code has functions for basic arithmetic operations. Add, subtract, multiply and divide
#add new functions as needed.

#The main functions is to find the total profit

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
    ans=b-a 
    return ans#FillinMissingCode

#main code


#we have sales data for a week. 
costOfCoffee, costOfTea, costOfVadai = 25,20,25

coffeeSales = [56,78,56,45,90, 103,120]
teaSales = [100,123,456,123,222,400,346]
vadaiSales = [23,45,67,12,89,90,120]

#Find total sales in the week.
#calculate avg sales for a week
employeeSalary = 500 #Rs500 per day

#calculate sales per week
totalsales=addTwoNumbers(addTwoNumbers(sum(coffeeSales),sum(teaSales)),sum(vadaiSales))

#calcuate sales per month
salespermonth=multiplyTwoNumbers(totalsales,4)

#calculate profit.
profit=subtractAfromB(salespermonth,employeeSalary)

#Call divide function to get the average from all three subjects
avg=divideAFromB(3,totalsales)
#FillinMissingCode

print("The avg sales is ", avg)
"""
Example
The avg sales is  2761
"""