# A Python program that read a sequence of words from the keyboard and print the words in the order they were entered.

def main():
    # initiate variables
    string_list = []
    
    # print the program title
    print("Enter the words and print the words in the order they were entered")
    print("Enter Exit to end input")

    # enter a sequence of words
    while True:
        word = str(input("Enter the words: "))
        if word == 'Exit':
            break
        else:
            string_list.append(word)

    # print the words in the order they were entered
    print("Print the words: ")
    for i in range(len(string_list)):
        print(string_list[i])

if __name__ == "__main__":
    main()