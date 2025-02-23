# A Python program to implement a simple calculator.

def calculator(operation, first_number, second_number):
    if operation == "addition":
        result = first_number + second_number
    elif operation == "subtraction":
        result = first_number - second_number
    elif operation == "multiplication":
         result = first_number * second_number
    elif operation == "division":
        if second_number == 0:
            print("The denominator cannot be 0 !")
            return 
        else: 
            result = first_number/second_number
    
    return result


def main():
    # print the program title
    print("A simple calculator")
    first_number = float(input("Input the first number: "))
    second_number = float(input("Input the second number: "))
    operation = input("Input the operation: ")
    # call the function and print the results
    if second_number == 0:
        calculator(operation, first_number, second_number)
    else:
        print("The result is: ", calculator(operation, first_number, second_number), sep = "")


if __name__ == "__main__":
    main()
