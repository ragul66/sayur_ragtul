"""Write a Python program to create a file where all letters of English alphabet are listed by specified 
number of letters on each line.
"""
def create_letter_file(letters_per_line, file_name):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    with open(file_name, 'w') as file:
        for i in range(0, len(alphabet), letters_per_line):
            line = alphabet[i:i+letters_per_line]
            file.write(line + '\n')

    print(f"The file '{file_name}' has been created.")


# Example usage
letters_per_line = 1
file_name = 'letter.txt'
create_letter_file(letters_per_line, file_name)
