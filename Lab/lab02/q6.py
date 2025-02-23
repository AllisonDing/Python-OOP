# A Python program that displays a solid triangle of symbols whose height is specified in integer parameter “height”, the symbol is specified in string parameter “symbol”.

def triangle_of_symbols(height, symbol):
    # number of spaces before symbol = height - i - 1
    # number of symbols = 2 * i + 1
    # number of spaces after symbol = height - i - 1

    for i in range(height):
        print(" " * (height - i - 1) + symbol * (2 * i + 1) + " " * (height - i - 1))


def main():
    # print the program title
    print("Print a solid triangle of symbols")
    # input the height and symbol
    height = int(input("Please enter the height of the triangle: "))
    symbol = input("Please enter the symbol of the triangle: ")
    # call the function and print the results
    triangle_of_symbols(height, symbol)


if __name__ == "__main__":
    main()