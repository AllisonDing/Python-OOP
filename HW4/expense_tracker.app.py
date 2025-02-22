from expense_tracker import Expense_Tracker

class ExpenseTrackerApp:
    def __init__(self) -> None:
        self.__expense_tracker = Expense_Tracker('CFO')
        self.__expense_tracker.read_employees_to_list()
        self.__expense_tracker.read_expenses_to_list()
        self.__expense_tracker.read_department_budget_to_list()
        self.__expense_tracker.create_department_list()
        self.__expense_tracker.create_expense_list()
        

    def show_menu(self) -> None:
        print("Menu")
        print("1. Add an employee")
        print("2. Modify an employee")
        print("3. Find an employee")
        print("4. Remove an employee")
        print("5. Add a department")
        print("6. Modify a department")
        print("7. Find a department")
        print("8. Remove a department")
        print("9. Input an expense")
        print("10. Create monthly expense report")
        print("11. Create monthly summary report")
        print("12. Create monthly expense for a specified category")
        print("13. Display highest expense employee for a certain month")
        print("14. Display department over budget limit for a certain month")
        print("15. Display highest expense department for a certain month")
        print("16. Alerts to department close to exceeding budget limit")
        print("17. Create total counts of expense category histogram for a specified department and for a certain month")
        print("18. Create department total monthly expense histogram for a certain month")
        print("19. Create employee total monthly expense histogram for a certain month")
        print("20. Modify budget for one category")
        print("21. Modify budget for all category")
        print("22. Display percentage used for each expense category (for all departments) for a certain month")
        print("23. Display employee expense by their ID")
        print("24. Exit")
        print(' ')

    def get_user_choice(self) -> int:
        output = int(input("Please enter your choice: "))
        return output
    
    def process_command(self, choice: int) -> None:
        if choice == 1:
            employee_id = int(input("Input employee ID: "))
            first_name = input("Input first name: ")
            last_name = input("Input last name: ")
            department_name = input("Input department name: ")
            rank = input("Input rank: ")
            self.__expense_tracker.add_employee(employee_id, first_name, last_name, department_name, rank)
        
        elif choice == 2:
            employee_id = int(input("Input employee ID: "))
            new_first_name = input("Input new first name: ")
            new_last_name = input("Input new last name: ")
            new_department_name = input("Input new department name: ")
            new_rank = input("Input rank: ")
            self.__expense_tracker.modify_employee(employee_id, new_first_name, new_last_name, new_department_name, new_rank)

        elif choice == 3:
            employee_id = int(input("Input employee ID: "))
            self.__expense_tracker.find_employee(employee_id)

        elif choice == 4:
            employee_id = int(input("Input employee ID: "))
            self.__expense_tracker.remove_employee(employee_id)

        elif choice == 5:
            name = input("Input department name: ")
            self.__expense_tracker.add_department(name)

        elif choice == 6:
            current_name = input("Input the current department name: ")
            new_name = input("Input the new department name: ")
            self.__expense_tracker.modify_department(current_name, new_name)

        elif choice == 7:
            name = input("Input department name: ")
            self.__expense_tracker.find_department(name)

        elif choice == 8:
            name = input("Input department name: ")
            self.__expense_tracker.remove_department(name)

        elif choice == 9:
            date_of_expense = input("Input date of expense: ")
            expense_amount = float(input("Input expense amount: "))
            expense_category = input("Input expense category: ")
            employee_id = int(input("Input employee ID: "))
            self.__expense_tracker.input_expense(date_of_expense, expense_amount, expense_category, employee_id)

        elif choice == 10:
            department = input("Input department name: ")
            month = input("Input month: ")
            self.__expense_tracker.monthly_expense_report(department, month)

        elif choice == 11:
            month = input("Input month: ")
            self.__expense_tracker.monthly_summary_report(month)            

        elif choice == 12:
            category = input("Input expense category: ")
            self.__expense_tracker.monthly_expense_for_specified_category(category) 

        elif choice == 13:
            month = input("Input month: ")
            self.__expense_tracker.highest_expense_employee(month) 

        elif choice == 14:
            month = input("Input month: ")
            self.__expense_tracker.department_over_budget_limit(month)

        elif choice == 15:
            month = input("Input month: ")
            self.__expense_tracker.highest_expense_department(month)

        elif choice == 16:
            self.__expense_tracker.alerts_exceeding_budget_limit()

        elif choice == 17:
            department = input("Input department name: ")
            month = input("Input month: ")
            self.__expense_tracker.total_counts_of_expense_category_histogram(department, month)

        elif choice == 18:
            month = input("Input month: ")
            self.__expense_tracker.department_total_monthly_expense_histogram(month)

        elif choice == 19:
            month = input("Input month: ")
            self.__expense_tracker.employee_total_monthly_expense_histogram(month)

        elif choice == 20:
            category = input("Input expense category: ")
            percentage = float(input("Input percentage you want to lower: "))
            self.__expense_tracker.modify_budget_for_one_category(category, percentage)

        elif choice == 21:
            percentage = float(input("Input percentage you want to lower: "))
            self.__expense_tracker.modify_budget_for_all_category(percentage)

        elif choice == 22:
            month = input("Input month: ")
            self.__expense_tracker.percentage_used_for_department_category(month)

        elif choice == 23:
            self.__expense_tracker.display_employee_expense_by_id()

        elif choice == 24:
            self.__expense_tracker.save_department_budgets_to_csv()
            self.__expense_tracker.save_employees_to_csv()
            self.__expense_tracker.save_expenses_to_csv()

        else:
            print("Please enter a valid choice!")

def main():
    app = ExpenseTrackerApp()
    print("=====================Expense Tracker=====================")
    print("There are a few things to notice: ")
    print("Firstly, when you enter a month, please use the first day of the month. For example, enter 2022-01-01 for Jan 2022.")
    print("Secondly, by default, the current month is September 2022 and budgets and expenses are only available between Jan 2022 and September 2022.")
    print("Thirdly, enter a float for percentage. For example, enter 0.1 for 10%")
    print("Lastly, the choice must be an integer.")
    
    while True:
        app.show_menu()
        choice = app.get_user_choice()
        app.process_command(choice)
        if choice == 24:
            break
        print()

if __name__ == "__main__":
    main()

