# A Python program that copies a one-dimensional list of n elements into a two-dimensional list of k rows and j columns.

def copy_1d_to_2dlist(onedlist, twodlist):
    # validate the two-dimensional list

    # length of one-dimensional list
    n = len(onedlist)
    # number of rows
    k = len(twodlist)
    # number of columns
    j = len(twodlist[0])

    if n != j * k:
        print("Error: they are not compatible!")
        return 
    
    # Copy numbers into two-dimensional list
    for r in range(k):     # iterate rows
        for c in range(j): # iterate columns
            twodlist[r][c] = onedlist[r * j + c]
    
    return twodlist

def main(onedlist, twodlist):
    # print the program title
    print("Copy a one-dimensional list of n elements into a two-dimensional list")
    # call the function and print the result
    print(copy_1d_to_2dlist(onedlist, twodlist))


if __name__ == "__main__":
    main([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]])


