# A Python program that prompts the user to enter an integer between 0 and 15 and display its corresponding hex number.


# build the mapping dictionary of number and letter for any value between 10 and 15
MyDict = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

# print the program title
print("An interger to hex number converter")

# input the value
number = int(input("Enter a decimal value (0 to 15): " ))

# if the value is between 0 and 9, the hex number is the same with the number
if number >= 0 and number <= 9:
    print("The hex value is", number, sep = " ")
# if the value is between 10 and 15, print the corresponding hex number using the dictionary 
elif number >= 10 and number <= 15: 
    print("The hex value is", MyDict[number], sep = " ")
# if the number is out of range, print error message
else:
    print("The value is out of range!")
