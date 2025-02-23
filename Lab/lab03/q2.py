# A menu-driven program that allows a user to enter a list of scores and then choose between finding the smallest, largest, sum, average or mode.

# Get a list of scores from the user input
def get_data():
       
    # input a list of scores and convert it into a score list
    scores = input("Please enter a list of scores (0 to 10) separated by space: ")
    score_list_str = scores.split(" ")
    score_list = []

    for score in score_list_str:
        score_list.append(int(score))

    return score_list

# Find the smallest, largest, sum, average or mode
def process_data(score_list):
    sm = 10
    lg = 0
    sum = 0
    for score in score_list:
        if score < sm:
            sm = score
        if score > lg:
            lg = score
        sum += score
    
    average = sum / len(score_list)

    # create the frequency array
    freq = {}

    # build the frequency array
    for score in score_list:
        if score in freq:
            freq[score] += 1
        else:
            freq[score] = 1
    
    # identify the mode
    mode = list(freq.keys())[0]
    for key in freq:
        if freq[key] > freq[mode]:
            mode = key

    return sm, lg, sum, average, mode

# Display a menu
def show_menu():
    print("1. Find the smallest score")
    print("2. Find the largest score")
    print("3. Find the sum")
    print("4. Find the average score")
    print("5. Find the mode score")
    print("6. Exit")
 
def main():
    # print the program title
    print("Finding the smallest, largest, sum, average, or mode from a list of scores")
    # input the score list
    score_list = get_data()
    # do the calculation
    sm, lg, sum, average, mode = process_data(score_list)
    
    # print the result for the choice
    while True:
        show_menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print ("The smallest number is", sm)
        elif choice == 2:
            print ("The largest number is", lg)
        elif choice == 3:
            print ("The sum is", sum)
        elif choice == 4:
            print ("The average score is", average)
        elif choice == 5:
            print ("The mode score is", mode)
        if choice == 6:
            print("Bye!")
            break
        if choice not in range(1, 7):
            print("Please enter a valid choice!")

if __name__ == "__main__":
    main()