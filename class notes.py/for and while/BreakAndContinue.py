############## Problem  1 #################### 
#Ask first friend the movies they like. Save it in a list
#Ask another friend the same question. If the movie is in the first friend's list, 
#Print "You both like "name of the color"
#Continue until they is atleast 3 movies they both like

#init variables
# Ask the first friend for the movies they like and save it in a list
"""movies = input("What movies do you like? (Separate multiple movies with commas): ").split(',')

# Convert movies into a list
movies_list = [movie.strip() for movie in movies]

common_movie_count = 0
common_movies = []

while True:
    # Ask the second friend for a movie
    movie = input("What movie do you like? ")

    # Check if the movie is in the first friend's list
    if movie in movies_list:
        common_movie_count += 1
        common_movies.append(movie)

        # Check if we reached the minimum count of common movies
        if common_movie_count >= 3:
            break
        else:
            print("You both like", movie)
    else:
        print("Try again")

# Print the list of common movies
print("Common movies:")
for movie in common_movies:
    print(movie)
"""

"""
What movies do you like? (Separate multiple movies with commas): blackthunder,marvel,antman
What movie do you like? marvel,galaxy,avengers
Try again
"""


############## Problem  2 #################### 
#Calculate the monthly salary for the phone salesman
#Base monthly pay Rs10000. 
#For every 5 phones sold, Rs 5000 bonus.
#For every phone aftr the first 5 phones, Rs1100 per phone bonus.
#If the salesman's salary is more than Rs20000 in the previous month and sells 20 or more phones 
# this month also, then he gets additional Rs5000.

monthlySalesList = [5,23,21,14,23,12,4,12,22,22,34,12]  # Sample number of phones sold in each month in a year

baseSalary = 10000
bonusPerFivePhones = 5000
bonusPerAdditionalPhone = 1100
additionalBonus = 5000

previousMonthSalary = baseSalary

for month, phoneCount in enumerate(monthlySalesList):
    # Calculate the Salary using If statements

    # Check if the salesman's salary is more than Rs20000 in the previous month and sells 20 or more phones
    # this month also, then he gets additional Rs5000.
    if previousMonthSalary > 20000 and phoneCount >= 20:
        currentMonthSalary = baseSalary + (bonusPerFivePhones * (phoneCount // 5)) + (bonusPerAdditionalPhone * (phoneCount - 5)) + additionalBonus
    else:
        currentMonthSalary = baseSalary + (bonusPerFivePhones * (phoneCount // 5)) + (bonusPerAdditionalPhone * (phoneCount - 5))

    print(f"This month's salary before additional bonus: {currentMonthSalary}")

    # Store the current month's salary as the previous month's salary for the next iteration
    previousMonthSalary = currentMonthSalary
"""
Example:
This month's salary before additional bonus: 15000
This month's salary before additional bonus: 49800
This month's salary before additional bonus: 52600
This month's salary before additional bonus: 29900
This month's salary before additional bonus: 54800
This month's salary before additional bonus: 27700
This month's salary before additional bonus: 8900
This month's salary before additional bonus: 27700
This month's salary before additional bonus: 53700
This month's salary before additional bonus: 53700
This month's salary before additional bonus: 76900
This month's salary before additional bonus: 27700

"""