# A Python program to display a solid rectangle of symbols whose height and weight are specified in integer parameter "height" and "weight" respectively.

def rectangle_of_symbols(height, weight, symbol):
    # display a solid rectangle of symbols
    for i in range(height):
        print(weight * symbol)

def main():
    # print the program title
    print('Print a rectangle of symbols')
    # input the height, weight, and symbol
    height = int(input("Enter the height: "))
    weight = int(input("Enter the weight: "))
    symbol = input("Enter the symbol: ")
    # call the function and print the results
    rectangle_of_symbols(height, weight, symbol)

if __name__ == "__main__":
    main()

