# A simple guessing game using Python


def guess(self, guess):
    self.__guess = guess

def unsuccessful_message():
    message = ["Your guess is low.", "Your guess is high."]
    return message
        
def successful_message():
    print("Congratulations! You did it.")

def sorry_message(RandomNumber):
    print("Sorry. The number was ", RandomNumber, '.', sep = "")
    print("You should have gotten it by now.")
    print("Better luck next time.")

def main():
    # print the program title
    print("A simple guessing game")
    
    # print the input message
    print("I am thinking of a number between 1 and 20.")
    
    # generate a random number between 1 and 20
    import random
    RandomNumber = random.randint(1, 20)

    # print the first try message
    guess = int(input("Can you guess what it is? "))
    
    # initiate the try variable to be 2 as this starts with our second try
    i = 1
    # print the results based on the situation
    while True:
    # if on the 5th try the guess is correct, then print congratulations message
        if i == 5 and guess == RandomNumber:
            successful_message()
            break

    # when tries > 5 the game is over
        elif i >= 5:
            sorry_message(RandomNumber)
            break

    # if guessing number is smaller than the random number
    # print the message that the guess is low and try again.
        elif i < 5:
            if guess < RandomNumber:
                print(unsuccessful_message()[0], end = "")
                guess = int(input(" Try again: "))
                i += 1

    # if guessing number is greater than the random number
    # print the message that the guess is high and try again.
            elif guess > RandomNumber:
                print(unsuccessful_message()[1], end = "")
                guess = int(input(" Try again: "))
                i += 1

    # if guessing number is equal to the random number
    # print the congratulations message 
            elif guess == RandomNumber:
                successful_message()
                break

if __name__ == "__main__":
    main()


    
