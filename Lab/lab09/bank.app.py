from bank import Bank
from customer import Customer

class BankApp:
    def __init__(self) -> None:
        self.__bank = Bank("SFBU Bank")
        self.__bank.read_customers_to_list()

    def show_menu(self) -> None:
        print("Menu")
        print("1. Add a client")
        print("2. Print all customers")
        print("3. Search and edit the client's inforamtion")
        print("4. Remove the client record")
        print("5. Print out a list of clients with last names that a user-specified last name")
        print("6. find the biggest and smallest account balance")
        print("7. Exit")

    def get_user_choice(self) -> int:
        output = int(input("Please enter your choice: "))
        return output
    
    def process_command(self, choice: int) -> None:

        if choice == 1:
            first_name = input("Please enter the customer's first name: ")
            last_name = input("Please enter the customer's last name: ")
            account_number = int(input("Please enter the customer's account number: "))
            account_balance = float(input("Please enter the customer's account balance: "))
            customer = Customer(first_name, last_name, account_number, account_balance)
            self.__bank.add_customer(customer)
            # self.__bank.display() # for test only

        elif choice == 2:
            option = int(input("1. forward or 2. backward: "))
            self.__bank.print_all(option)
        
        elif choice == 3:
            account_number = int(input("Please enter the customer account number that you would like to edit: "))
            first_name = input("Please enter the first name you would like to change into: ")
            last_name = input("Please enter the last name you would like to change into: ")
            account_balance = float(input("Please enter the account balance that you would like to change into: "))
            self.__bank.update_customer(Customer(first_name, last_name, account_number, account_balance))
        
        elif choice == 4:
            account_number = int(input("Please enter the customer account number that you would like to remove: "))
            self.__bank.remove_customer(account_number)

        elif choice == 5:
            last_name = input("Please enter the last name you would like to search: ")
            self.__bank.print_last_name(last_name)

        elif choice == 6:
            option = int(input("1. biggest or 2. smallest: "))
            self.__bank.biggest_and_smallest_balance(option)

        elif choice == 7:
            self.__bank.save_customers_to_csv()

        else:
            print("Please enter a valid choice!")


def main():
    app = BankApp()
    while True:
        app.show_menu()
        choice = app.get_user_choice()
        app.process_command(choice)
        if choice == 7:
            break
        print()

if __name__ == '__main__':
    main()

