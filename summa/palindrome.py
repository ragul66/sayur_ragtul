def palindrome(str):
    return str==str[::-1]

str="malayalam"
ans=palindrome(str)

if ans:
    print("yes")
else:
    print("NO")






























# def palindrome(str):
#     if len(str) < 2:
#         return True
#     elif str[0] != str[-1]:
#         return False
#     else:
#         return palindrome(str[1:-1])
    
# str = "racecar"
# if palindrome(str):
#     print(str, "is a palindrome")
# else:
#     print(str, "is not a palindrome")


