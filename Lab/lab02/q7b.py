# A Python program that read a sequence of words from the keyboard and print the words in the order they were entered.

def main():
    # initiate variables
    string_list = []
    
    # the program title
    print("Enter the words and print the unique and sorted words")
    print("Enter Exit to end input")

    # enter a sequence of words
    while True:
        word = str(input("Enter the words: "))
        if word == 'Exit':
            break
        else:
            string_list.append(word)
    
    # sort the words and remove the duplicate words
    string_list = list(sorted(set(string_list)))

    # print the sorted unique words
    print("Print the words: ")
    for i in range(len(string_list)):
        print(string_list[i])

if __name__ == "__main__":
    main()

