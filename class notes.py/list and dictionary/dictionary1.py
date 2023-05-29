########## Program 1
#find the list unique words in a sentence
#hint - Each word is a key, count is the value

sentence = "This is a cat and it has a tail and two eyes"

countOfWords = {}  # Create an empty dictionary to store word counts

# Split the sentence into words
words = sentence.split()

# Iterate over each word in the list
for word in words:
    if word in countOfWords:
        countOfWords[word] += 1  # Increment the count if the word already exists
    else:
        countOfWords[word] = 1  # Add the word to the dictionary with a count of 1

print(countOfWords)

########## Program 2
#