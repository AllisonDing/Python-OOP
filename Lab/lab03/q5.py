# A Python program that displays a 4 option menu the print the results.

# Display a menu
def show_menu():
    print("e - Enter a new employee's information")
    print("a - Display all employees information")
    print("d - Display an employee's information")
    print("q - Quit")
 

def main():
    # print the program title
    print("Create a program that displays a 4 option menu and print the results. When you enter the information, please separate them by a space.")
    
    # list that contains all the employee list
    employees = []
    
    while True:
        show_menu()
        option = str(input("Enter your option: "))
        
        # option e will allow input of an employee information 
        # this process can repeat multiple times and the results will be saved
        if option == 'e':
            employee_str = str(input("Please enter the name, ID, department number, and age of an employee: "))
            
            # create the employee list that contains an employee's name, ID, department number, and age of this employee
            employee = []
            
            for _ in employee_str.split(" "):
                employee.append(_)
            # add the employee list to the employees list
            employees.append(employee)
        
        # option a will print all the employees information
        elif option == 'a':
            print(employees)
        
        # option d will input an employee's name and print that employee's information if that employee's information is available
        elif option == 'd':
            search_by_name = str(input("Please enter the employee's name: "))
            
            # create the list that contains all the existing employee names
            name_list = []
            for employee in employees:
                name_list.append(employee[0])
            
            # evaluate if the employee information can be found. If the employee can be found, then print the employee information
            if search_by_name in name_list:
                for employee in employees:
                    if employee[0] == search_by_name:
                        print(employee)
            
            # if that employee cannot be found, program will ask if you would like to input a new employee's information
            elif search_by_name not in name_list: 
                new_employee_y_n = str(input("This employee is not found. Would you like to enter a new employee (y/n)? "))
                # if the answer is 'y', then input the new employee's information
                if new_employee_y_n == 'y':
                        
                    new_employee = []
                    new_employee_str = str(input("Please enter the name, ID, department number, and age of an employee: "))
                        
                    for _ in new_employee_str.split(" "):
                        new_employee.append(_)
                    # add the employee list to the employees list
                    employees.append(new_employee)
                    
                else: 
                    continue

        
        # option q will quit the program
        elif option == 'q':
            print("Bye!")
            break
        
        # if the input is not one of the option e, a, d, q, print the error message
        elif option not in ('e', 'a', 'd', 'q'):
            print("Please enter a valid option!")


if __name__ == "__main__":
    main()