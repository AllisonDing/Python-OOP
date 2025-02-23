# A Python program to calculate the trace of a square matrix (i.e. a two-dimensional list with the same number of rows as columns)

# initiate variables
number_of_columns = 0
trace_of_matrix = 0

def trace(matrix):
    # calculate the number of columns (and/or rows) of the square matrix
    global number_of_columns
    number_of_columns = len(matrix)

    # calculate the trace of the square matrix
    global trace_of_matrix
    for i in range(number_of_columns):
        trace_of_matrix += matrix[i][i]

    return trace_of_matrix

def main(matrix):
    # print the program title
    print("Calculate the trace of a square matrix")
    # call the function and print the trace of the square matrix
    print("The trace of the square matrix is: ", trace(matrix), sep = "")


if __name__ == "__main__":
    main(
[[4, 6, 7, 3, 2],
[7, 5, 8, 5, 6],
[8, 2, 5, 2, 1],
[3, 3, 6, 6, 7],
[6, 4, 9, 5, 7]])





