'''1. In the input, find the first A and last A, print all the letters between these two A. 
  If there is no A or 2nd A is not found, find the first B  and last B and print all the letters between these two B. 
  If there is no B or 2nd B is not found, find the first C and last C and print all the letters between these two C.''' 


word=input("Enter your word").lower()
#i=a.split()
for i in word:
       for a in i:
            print(a)
       
        



# # function to determine the score of a single roll
# def roll_score(pins):
#     return pins

# # function to determine the score of a frame
# def frame_score(roll1, roll2):
#     if roll1 == 10:
#         return 10 + roll_score(roll2) + roll_score(roll3)
#     elif roll1 + roll2 == 10:
#         return 10 + roll_score(roll3)
#     else:
#         return roll_score(roll1) + roll_score(roll2)

# # function to determine the total score of the game
# def game_score(rolls):
#     total_score = 0
#     roll_index = 0
#     for frame in range(10):
#         if rolls[roll_index] == 10:
#             total_score += frame_score(rolls[roll_index], 0, rolls[roll_index+1])
#             roll_index += 1
#         else:
#             total_score += frame_score(rolls[roll_index], rolls[roll_index+1])
#             roll_index += 2
#     return total_score

# # example usage
# rolls = [10, 7, 3, 9, 0, 10, 0, 8, 8, 2, 0, 6, 10, 10, 10, 8, 1]
# print("Total score:", game_score(rolls))
