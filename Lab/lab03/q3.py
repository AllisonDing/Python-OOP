# A Python program that get the width (maximum number of asterisks) as an input and creates the following pattern. 

# initiate variables
number_of_spaces = 0
number_of_asterisks = 0

# let n be the maximum number of asterisks

# when i between 0 and n - 1
# number of spaces = n - i - 1
# number of asterisks = i + 1

# when i between n and 2n - 2
# number of spaces = i + n  + 1
# number of asterisks same with 2n - i index

def space_calculation(n, i):
    if i <= n - 1:
        return n - (i + 1)
    elif i >= n:
        return i - (n - 1)

def asterisk_calculation(n, i):
    if i <= n - 1:
        return i + 1
    elif i >= n:
        return 2*n - i - 1 

# print the program title
print("A python program that get the width (maximum number of asterisks) as an input and creates the following pattern")

def main():
    # input the maximum number of asterisks.
    n = int(input("Enter the maximum number of asterisks: "))
    for i in range(2*n - 1): # number of rows = 2n - 1
        print(" "*space_calculation(n, i) + "*"*asterisk_calculation(n, i))


if __name__ == "__main__":
    main()

