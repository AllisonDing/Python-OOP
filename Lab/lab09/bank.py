    
from customer import Customer
from db import CustomerRepository
    
class Bank:
    def __init__(self, bank_name: str) -> None:
        self.__bank_name = bank_name
        self.__customers: list[Customer] = []
    
    def read_customers_to_list(self) -> None:
        Customer = CustomerRepository()
        self.__customers = Customer.read_customers()

    def save_customers_to_csv(self) -> None:
        Customer = CustomerRepository()
        Customer.write_customers(self.__customers)

    def add_customer(self, customer: Customer) -> None:
        self.__customers.append(customer)
        # export the newly added customer to DB csv

    def remove_customer(self, account_number: int) -> None:
        found = False
        for c in self.__customers:
            if c.account_number == account_number:
                self.__customers.remove(c)
                found = True
        
        if found == False:
            print("Could not find the customer!")

    def print_all(self, option: int) -> None:

        lst = []
        for c in self.__customers:
            lst.append(c.account_number)
        lst = sorted(lst)
        lst_reversed = reversed(lst)
        
        if option == 1:
            for l in lst:
                for c in self.__customers:
                    if l == c.account_number:
                        c.display()

        elif option == 2:
            for l in lst_reversed:
                for c in self.__customers:
                    if l == c.account_number:
                        c.display()

    def update_customer(self, customer: Customer) -> None:
        found = False
        for c in self.__customers:
            if c.account_number == customer.account_number:
                c.first_name = customer.first_name
                c.last_name = customer.last_name
                c.account_balance = customer.account_balance
                found = True
        
        if found == False:
            print("Could not find the account number!")
    
    def print_last_name(self, last_name: str) -> None:
        found = False
        for c in self.__customers:
            if c.last_name == last_name:
                c.display()
                found = True
        
        if found == False:
            print("Could not find the last name!")
    
    def biggest_and_smallest_balance(self, option: int) -> None:

        if option == 1:
            biggest = self.__customers[0].account_balance
            for e in self.__customers:
                if e.account_balance > biggest:
                    biggest = e.account_balance
            print(biggest) 
        
        if option == 2:
            smallest = self.__customers[0].account_balance
            for e in self.__customers:
                if e.account_balance < smallest:
                    smallest = e.account_balance
            print(smallest)
        
    # def display(self) -> None:
    #     print(f"bank_name = {self.__bank_name}")
    #     for c in self.__customers:
    #         c.display()

# def main():
#     b = Bank('sfbu')
#     b.read_customers_to_list()
#     b.display()
    
#     c = Customer('Allison', 'Ding', 999, 900)
#     b.add_customer(c)
#     b.display()
#     b.save_customers_to_csv()


# if __name__ == '__main__':
#     main()
    





    

        




    
