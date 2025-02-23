# A Python program that stores votes for the survey and aggregates the votes result

def main():
    # print the program title
    print("The survey of food menu")
    # input the menu
    menu = ["Pizza", "Hot Dog", "Ham", "Cheese"]

    # create a 2-D array of votes (Like, Dislike)
    votes = [
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0]
        ]

    while True:
        # input number of likes and dislikes and aggregate the results and store in the votes table
        for i in range(len(menu)):
            vote = input("Do you like " + menu[i] + " (y/n)? ")
            if vote == 'y':
                votes[i][0] += 1
            else:
                votes[i][1] += 1

        conf = input("Do you have another student (y/n)? ")
        if conf == 'n':
            break
    
    # print the results in a tabular format
    print("{:<16} {:<8} {:<8}".format('', 'Like', 'Dislike'))

    for i in range(len(menu)):
        print("{:<16} {:<8} {:<8}".format(menu[i], votes[i][0], votes[i][1]))
    

if __name__ == "__main__":
    main()



