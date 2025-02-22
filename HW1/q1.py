# A Python program that inputs a single letter and prints out the corresponding digit on the telephone

# mapping dictionary of digit and letters
MyDict = {2:"ABC", 3:"DEF", 4:"GHI", 5:"JKL", 6:"MNO", 7:"PRS", 8:"TUV", 9:"WXY"}

# print the program title
print("A python program that inputs a single letter and prints out the corresponding digit on the telephone")

# input a letter
print("Enter a single letter, and I will tell you what the corresponding digit is on the telephone.")
letter = str(input()) 

# print message indicating that there is no matching digit for any nonalphabeti character. 
if not letter.isalpha():
    print("There is no matching digit for any nonalphabetic character!")
# print message indicating that the lowercase letters are invalid characters.
elif letter == letter.lower():
    print("The lowercase letters are invalid characters!")
# print message indicating that no digit corresponds to either Q or Z.
elif letter in ("Q", "Z"):
    print("There is no digit on the telephone that corresponds to", letter, sep = " ")
# print the results when the user enters a good letter.
else:
    for key, value in MyDict.items():
        if letter in value:
            print("The digit", key, "corresponds to the letter", letter, "on the telephone.", sep = " ") 