from expense import Expense
from employee import Employee
from department_budget import Department_Budget
import csv

class ExpenseRepository:
    def __init__(self, filename: str = "expense.csv") -> None:
        self.__filename = filename
    
    # read customer data from the csv file and return a list of customer objects
    def read_expenses(self) -> list[Expense]:
        expenses: list[Expense] = []

        with open(self.__filename, newline = "") as file:
            reader = csv.reader(file)
            
            # Each row is a list of strings
            for row in reader:
                expense = Expense(row[0], float(row[1]), row[2], int(row[3]))
                expenses.append(expense)

        return expenses
    
    def write_expenses(self, expenses: list[Expense]) -> None:
        with open(self.__filename, "w", newline = "") as file:
            writer = csv.writer(file)
            for expense in expenses:
                writer.writerow(expense.get_csv())
    

class EmployeeRepository:
    def __init__(self, filename: str = "employee.csv") -> None:
        self.__filename = filename
    
    # read customer data from the csv file and return a list of customer objects
    def read_employees(self) -> list[Employee]:
        employees: list[Employee] = []

        with open(self.__filename, newline = "") as file:
            reader = csv.reader(file)
            
            # Each row is a list of strings
            for row in reader:
                employee = Employee(int(row[0]), row[1], row[2], row[3], row[4])
                employees.append(employee)

        return employees
    
    def write_employees(self, employees: list[Employee]) -> None:
        with open(self.__filename, "w", newline = "") as file:
            writer = csv.writer(file)
            for employee in employees:
                writer.writerow(employee.get_csv())


class DepartmentBudgetRepository:
    def __init__(self, filename: str = "department_budget.csv") -> None:
        self.__filename = filename
    
    # read customer data from the csv file and return a list of customer objects
    def read_department_budgets(self) -> list[Department_Budget]:
        department_budgets: list[Department_Budget] = []

        with open(self.__filename, newline = "") as file:
            reader = csv.reader(file)
            
            # Each row is a list of strings
            for row in reader:
                department_budget = Department_Budget(row[0], row[1], float(row[2]))
                department_budgets.append(department_budget)

        return department_budgets
    
    def write_department_budgets(self, department_budgets: list[Department_Budget]) -> None:
        with open(self.__filename, "w", newline = "") as file:
            writer = csv.writer(file)
            for department_budget in department_budgets:
                writer.writerow(department_budget.get_csv())

class DepartmentBudgetRepositoryOld:
    def __init__(self, filename: str = "department_budget_old.csv") -> None:
        self.__filename = filename
    
    # read customer data from the csv file and return a list of customer objects
    def read_department_budgets(self) -> list[Department_Budget]:
        department_budgets: list[Department_Budget] = []

        with open(self.__filename, newline = "") as file:
            reader = csv.reader(file)
            
            # Each row is a list of strings
            for row in reader:
                department_budget = Department_Budget(row[0], row[1], float(row[2]))
                department_budgets.append(department_budget)

        return department_budgets
    
    def write_department_budgets(self, department_budgets: list[Department_Budget]) -> None:
        with open(self.__filename, "w", newline = "") as file:
            writer = csv.writer(file)
            for department_budget in department_budgets:
                writer.writerow(department_budget.get_csv())




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
    