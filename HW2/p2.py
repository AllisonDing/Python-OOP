# Given a square matrix filled with elements of 0 or 1 randomly, find the first square submatrix with all 1 elements. 
# This square submatrix should be as big as it can be, but it must include only ones and be at least 3 in size.

def search_first_squareblock(matrix: list[list[int]]) -> tuple[int, int, int]:
    size = len(matrix) # size of the matrix
    threshold = 3 # the square submatrix must be at least 3 in size 
    result_list = [] # result list that stores all the square submatrix that is at least 3 in size

    def helper(pos_i: int, pos_j: int, threshold: int) -> int: # helper function to calculate the sum of the squares (with certain position as starting point). 
        sum = 0
        for i in range( pos_i, pos_i + threshold):
            for j in range(pos_j, pos_j + threshold):
                sum += matrix[i][j]
        return sum
    
    for threshold in range(threshold, size + 1): # loop over different values of threshold (between 3 and size of matrix)
        for i in range(size - threshold + 1):
            for j in range(size - threshold + 1):
                sum = helper(i, j, threshold) # calculate the sum of the squares (with certain position as starting point)
                if sum == threshold ** 2: # if sum is equal to square of threshold, then the submatrix meets the requirement
                    result_list.append((i, j, threshold)) # return the starting position and threshold to the reuslt list

    # identify the largest threshold that the square submatrix can meet the requirement
    # the first element in the result list has the starting position the first square submatrix is located
    # we just need to find the largest threshold it can be.            
    largest = 0
    for result in result_list:
        if result[0] == result_list[0][0] and result[1] == result_list[0][1]:
            largest = max(largest, result[2])
    
    return result_list[0][0], result_list[0][1], largest

def main():
    # input the size of the matrix
    size = int(input("Enter the number of rows in the matrix: "))
    # input the matrix row by row
    print("Enter the matrix row by row:")
    matrix = []
    for i in range(size):
        string = str(input())
        row = [int(char) for char in string]
        matrix.append(row)
    
    # call function and print result
    result = search_first_squareblock(matrix)
    print("The first suqare submatrix is at (", result[0],", ", result[1], ") with size ", result[2], sep = "")


if __name__ == "__main__":
    main()
