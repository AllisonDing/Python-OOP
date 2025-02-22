# A Python program that evaluates a five-digit integer is a Palindrome or not.


# print the program title
print("A Palindrome evaluation program")

# input a five-digit integer
number = int(input("Enter a five-digit integer: "))


def isPalindrome(number:int):
    # exception case
    if number < 0: 
        return False
    
    # calculate the dividor, 10000
    div = 10 ** (len(str(number)) - 1)
    # repeat until we have compared each pair of digits (last vs. first, fourth vs. second)
    while number:
        # use remainder to get the last digit
        last = number % 10
        # use dividor to get the first digit
        first = number // div
        # if the last and the first digit not the same return False 
        if first != last:
            return False
        # remove the last and the first digit and get the new number
        number = (number % div) // 10
        # re-calculate the divisor by 100 because we remove two digits 
        div = div / 100
    
    return True
# print the results
print("It is a palindrome:", isPalindrome(number), sep = " ")


