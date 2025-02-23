from customer import Customer
import csv

class CustomerRepository:
    def __init__(self, filename: str = "customers.csv") -> None:
        self.__filename = filename
    
    # read customer data from the csv file and return a list of customer objects
    def read_customers(self) -> list[Customer]:
        customers: list[Customer] = []

        with open(self.__filename, newline = "") as file:
            reader = csv.reader(file)
            
            # Each row is a list of strings
            for row in reader:
                customer = Customer(row[0], row[1], int(row[2]), float(row[3]))
                customers.append(customer)

        return customers
    
    def write_customers(self, customers: list[Customer]) -> None:
        with open(self.__filename, "w", newline = "") as file:
            writer = csv.writer(file)
            for customer in customers:
                writer.writerow(customer.get_csv())
    

# def main():
#     db = CustomerRepository()
#     customers = db.read_customers()
#     for customer in customers:
#         print(customer)

#     customer = Customer("Jack", "Li", 444, 300)
#     customers.append(customer)

#     db.write_customers(customers)


# if __name__ == '__main__':
#     main()