############## Problem  1 #################### 
#Ask first friend the colors they like. Save it in a list
#Ask another friend the same question. If the color is in the first friend's list, 
#Print "You both like "name of the color"
#If it is not in the first friend's list, Save it another list.



first_friend_colors = []
second_friend_colors = []
common_colors = []

# Ask first friend for their favorite colors
num_colors = int(input("How many favorite colors does the first friend have? "))

for color in range(num_colors):
    color = input("Enter a favorite color: ")
    first_friend_colors.append(color)

# Ask second friend for their favorite colors
num_colors = int(input("How many favorite colors does the second friend have? "))

for color in range(num_colors):
    color = input("Enter a favorite color: ")
    second_friend_colors.append(color)

# Check for common colors
for color in second_friend_colors:
    if color in first_friend_colors:
        common_colors.append(color)

# Print the common colors
if common_colors:
    print("You both like the following colors:")
    for color in common_colors:
        print(color)
else:
    print("You both have different favorite colors.")

# Print the colors that are not in the first friend's list
if second_friend_colors:
    print("Colors that are not in the first friend's list:")
    for color in second_friend_colors:
        if color not in first_friend_colors:
            print(color)

"""
Example
How many favorite colors does the first friend have? 3 
Enter a favorite color: red
Enter a favorite color: white
Enter a favorite color: black
How many favorite colors does the second friend have? 4
Enter a favorite color: white
Enter a favorite color: orange
Enter a favorite color: yellow
Enter a favorite color: blue
You both like the following colors:
white
Colors that are not in the first friend's list:
orange
yellow
blue
"""

############## Problem 2 ####################
#Ask the user how many members in the family. Get Name, age and height and weight.
#add the details into four lists.
#Print the each memeber of the family and their details
#eg output 
# Name      Age     Height(cm)      Weight(kg)
# Ram       35      180             80
# Seetha    34      145             58
#
nameList = []
ageList = []
heightList=[]
weightList=[]
#FillinMissingCode for other data
noOfPeople = int (input("How many people in the family"))
for member in range (1, noOfPeople + 1):
    details = input(f"Enter the details of member {member} Name, age, height, weight")
    #FillinMissingCode Split the input string and add it to the lists
    name, age, height, weight = details.split()
    nameList.append(name)
    ageList.append(int(age))
    heightList.append(float(height))
    weightList.append(float(weight))
#print the header 
print ("Name\t\tAge\t\tHeight(cm)\t\tWeight(kg)") #learn about \t
for index, member in enumerate(nameList): #Learn how enumerate works
   print(f"{nameList[index]}\t\t{ageList[index]}\t\t{heightList[index]}\t\t{weightList[index]}")


"""
Example
How many people in the family2
Enter the details of member 1 Name, age, height, weightmuthukumar 51 165 66
Enter the details of member 2 Name, age, height, weightvasanthi 42 150 65
Name            Age             Height(cm)              Weight(kg)
muthukumar              51              165.0           66.0
vasanthi                42              150.0           65.0
"""
