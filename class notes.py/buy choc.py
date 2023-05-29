#buy choc and cake
# one choc is Rs 200
# one cake is 150
#get budget from user.

#find how many choc and cake the user can buy

noOfCake = 0
noOfChoc = 0

#get budget from user
money = float(input("Enter your budget: "))

while money >= 150:
    if money >= 200:
        #buy chocolate
        noOfChoc += 1
        money -= 200
    else:
        #buy cake
        noOfCake += 1
        money -= 150

#print the number of cakes and chocolates
print("Number of cakes:", noOfCake)
print("Number of chocolates:", noOfChoc)

"""
Example
Enter your budget: 600
Number of cakes: 0
Number of chocolates: 3
"""