# A Pytho program to develop an app.
# The app should have a nice user-friendly menu with described options for the user to select.

def menu(): # menu
    print("Please enter the option:")
    print("a: Create a new account")
    print("b: Display the account information")
    print("c: Change account information")
    print("d: Print the account list")
    print("e: Exit")

class Account: # Define Account class
    def __init__(self, firstName: str, lastName: str, accountNumber: int, balance: float):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__accountNumber = accountNumber
        self.__balance = balance # balance can be negative
        if accountNumber < 0:
            raise ValueError("Account Number is a positive integer!")
    
    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, new_first_name: str) -> None:
        self.__firstName = new_first_name
    
    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, new_last_name: str) -> None:
        self.__lastName = new_last_name
    
    @property
    def accountNumber(self) -> int:
        return self.__accountNumber
    
    @property
    def balance(self) -> float:
        return self.__balance

    @balance.setter
    def balance(self, new_balance: float) -> None:
        self.__balance = new_balance

    def __str__(self) -> str: # create print out
        return f"Account First Name = {self.__firstName}, Last Name = {self.__lastName}, Account Number = {self.__accountNumber}, Balance = {self.__balance}"

    def __repr__(self) -> str:
        return str(self)


def option_a():
    firstName = str(input("Enter the first name: "))
    lastName = str(input("Enter the last name: "))
    accountNumber = int(input("Enter the account number: "))
    balance = float(input("Enter the balance: "))
    return Account(firstName, lastName, accountNumber, balance)

def option_b():
    checkAccountNumber = int(input("Enter the account number: "))
    return checkAccountNumber

def option_c():
    changeAccountNumber = int(input("Enter the account number: "))
    return changeAccountNumber



def main():
    account_list = [] # initiate list of account object
    while True:
        menu() # print menu
        option = str(input()) # input option
        # option a: The software should prompt the user to enter their first name, last name, account number, and account balance when creating a new account.
        if option == "a": 
            new_acct = option_a()

            found = False
            for acct in account_list:
                if acct.accountNumber == new_acct.accountNumber and acct.firstName == new_acct.firstName and acct.lastName == new_acct.lastName and acct.balance == new_acct.balance:
                    print("The account already exists!")
                    found = True
                    break
            if found == False:
                account_list.append(new_acct)
            
            print()
        # option b: The app should request the user to input their account number and, if one is found, display the account information.
        elif option == "b":
            checkAccountNumber = option_b()
            
            found = False
            for acct in account_list:
                if acct.accountNumber == checkAccountNumber:
                    print(acct)
                    found = True
                    break
            if found == False:
                print("The account cannot be found!")

            print()
        # option c: To change account information, the app should prompt the user to enter the account number, 
        # if one is present, and then prompt the user to enter the new first name, last name, and account balance information.
        elif option == "c":
            changeAccountNumber = option_c()
            found = False
            for acct in account_list:
                if acct.accountNumber == changeAccountNumber:
                    # account_list.remove(acct) 
                    new_first_name = str(input("Enter the new first name: "))
                    new_last_name = str(input("Enter the new last name: "))
                    new_balance = float(input("Enter the new balance: "))
                    acct.firstName = new_first_name
                    acct.lastName = new_last_name
                    acct.balance = new_balance
                    # account_list.append(Account(new_first_name, new_last_name, changeAccountNumber, new_balance))
                    found = True
                    break
            if found == False:
                print("The account cannot be found!")

            print()
        # option d: It should also give the bank staff the ability to print a list of all accounts backwards and forwards based on the account number.
        elif option == "d":
            print(account_list)
            list = []
            for acct in account_list:
                list.append(acct.accountNumber)
            # order account list in alphbetically ascending order and descending order
            forward_list = sorted(list, reverse = False)
            backward_list = sorted(list, reverse = True)
            
            forward = []
            backward = []
            
            for f in forward_list:
                for acct in account_list:
                    if f == acct.accountNumber:
                        forward.append(acct)
                    
            for f in backward_list:
                for acct in account_list:
                    if f == acct.accountNumber:
                        backward.append(acct)

            how = str(input("How would you like to print the list of accounts (forward/backward)? "))
            
            if how == "forward":
                print(forward)
                print()
            elif how == "backward":
                print(backward)
                print()
            else:
                print("No such an option!")
                print()

        else:
            break

if __name__ == "__main__":
    main()

        
     