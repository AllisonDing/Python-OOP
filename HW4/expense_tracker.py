from employee import Employee
from expense import Expense
from department import Department
from department_budget import Department_Budget
from db import EmployeeRepository, ExpenseRepository, DepartmentBudgetRepository, DepartmentBudgetRepositoryOld

class Expense_Tracker:
    def __init__(self, user_name: str) -> None:
        self.__user_name = user_name
        self.__departments: list[Department] = []
        self.__expenses = {}
        self.__expenses_readin: list[Expense] = []
        self.__department_budgets_readin: list[Department_Budget] = []
        self.__old_department_budgets_readin: list[Department_Budget] = []
        self.__employees_readin: list[Employee] = []

    @property
    def departments(self) -> list[Department]:
        return self.__departments
    
    @property
    def expenses(self):
        return self.__expenses
    
    @property
    def expenses_readin(self) -> list[Expense]:
        return self.__expenses_readin

    @property
    def department_budgets_readin(self) -> list[Department_Budget]:
        return self.__department_budgets_readin

    @property
    def old_department_budgets_readin(self) -> list[Department_Budget]:
        return self.__old_department_budgets_readin   

    @property
    def employees_readin(self) -> list[Employee]:
        return self.__employees_readin    

    def read_department_budget_to_list(self) -> None:
        Department_Budget_Repo = DepartmentBudgetRepository()
        self.__department_budgets_readin = Department_Budget_Repo.read_department_budgets()

    def read_old_department_budget_to_list(self) -> None:
        Department_Budget_Repo_Old = DepartmentBudgetRepositoryOld()
        self.__old_department_budgets_readin = Department_Budget_Repo_Old.read_department_budgets()

    def read_employees_to_list(self) -> None:
        Employee_Repo = EmployeeRepository()
        self.__employees_readin = Employee_Repo.read_employees()

    def read_expenses_to_list(self) -> None:
        Expense_Repo = ExpenseRepository()
        self.__expenses_readin = Expense_Repo.read_expenses()

    def create_department_list(self):
        unique_dept_lst = []
        for b in self.department_budgets_readin:
            if b.department_name not in unique_dept_lst:
                unique_dept_lst.append(b.department_name)
        
        # create initial department list
        for name in unique_dept_lst:
            self.__departments.append(Department(name))
        
        # add initial employee list to departments
        for department in self.__departments:
            for employee in self.employees_readin:
                if department.name == employee.department_name:
                    department.employees.append(Employee(employee.employee_id, employee.first_name, employee.last_name, employee.department_name, employee.rank))
        
        # add initial department budgets to departments
        for department in self.__departments:
            for b in self.department_budgets_readin:
                if department.name == b.department_name:
                    department.department_budgets.update({b.expense_category: b.budget}) 

    def create_expense_list(self) -> None:
        for d in self.departments:
            expense_list = [] 
            for e in d.employees:
                for expense in self.expenses_readin:
                    if e.employee_id == expense.employee_id:
                        expense_list.append(expense)
            self.expenses.update({d.name:expense_list})

    def save_employees_to_csv(self) -> None:
        Employee_Repo = EmployeeRepository()
        employee_lst = []
        for d in self.departments:
            employee_lst += d.employees
        Employee_Repo.write_employees(employee_lst)

    def save_expenses_to_csv(self) -> None:
        Expense_Repo = ExpenseRepository()
        expense_lst = []
        for key, value in self.expenses.items():
            expense_lst += value
        Expense_Repo.write_expenses(expense_lst)

    def save_department_budgets_to_csv(self) -> None:
        Department_Budget_Repo = DepartmentBudgetRepository()
        db_lst = []
        for d in self.departments:
            for key, value in d.department_budgets.items():
                db = Department_Budget(d.name, key, value)
                db_lst.append(db)
        Department_Budget_Repo.write_department_budgets(db_lst)

    def add_employee(self, employee_id: int, first_name: str, last_name: str, department_name: str, rank: str) -> None:
        # employee
        employee = Employee(employee_id, first_name, last_name, department_name, rank)
        found = False
        for d in self.departments:
            for e in d.employees:
                if e == employee:
                    found = True
                    print("The employee already exists!")
        if found == False:
            for d in self.departments:
                if d.name == department_name:
                    d.employees.append(employee)
                    print("The employee is successfully added!")

    def modify_employee(self, employee_id: int, new_first_name: str, new_last_name: str, new_department_name: str, new_rank: str) -> None:
        # employee
        found = False
        for d in self.departments:
            for e in d.employees:
                if e.employee_id == employee_id:
                    found = True
                    d.employees.remove(e)        
        if found == False:
            print("The employee does not exist!")
        
        # new employee could be in a different department, thus we need to first remove the old employee and then add the new employee.
        employee = Employee(employee_id, new_first_name, new_last_name, new_department_name, new_rank)
        for d in self.departments:
            if d.name == new_department_name:
                d.employees.append(employee)
                print("The employee is successfully modified!")

    def find_employee(self, employee_id: int) -> None:
        # employee
        found = False
        for d in self.departments:
            for e in d.employees:
                if e.employee_id == employee_id:
                    found = True
                    print(e)
        if found == False:
            print("The employee does not exist!")

    def remove_employee(self, employee_id: int) -> None:
        # employee
        found = False
        for d in self.departments:
            for e in d.employees:
                if e.employee_id == employee_id:
                    found = True
                    d.employees.remove(e)
                    print("The employee is successfully removed!")
    
        if found == False:
            print("The employee does not exist!")

    def add_department(self, name: str) -> None:
        new_department = Department(name)
        found = False
        for d in self.departments:
            if  d == new_department:
                found = True
                print("The department already exists!")
        if found == False:
            self.departments.append(new_department)
            print("The department is successfully added!")

    def modify_department(self, current_name: str, new_name: str) -> None:
        # department
        found = False
        for d in self.departments:
            if d.name == current_name:
                found = True
                d.name = new_name
                print("The department is successfully modified!")
        if found == False:
            print("The department does not exist!")

    def find_department(self, name: str) -> None:
        # department
        found = False
        for d in self.departments:
            if d.name == name:
                found = True
                print(d)
        if found == False:
            print("The department does not exist!")

    def remove_department(self, name: str) -> None:
        # department
        found = False
        remove_department = Department(name)
        for d in self.departments:
            if d == remove_department:
                found = True
                self.departments.remove(remove_department)
                print("The department is successfully removed!")
        if found == False:
            print("The department does not exist!")

    def input_expense(self, date_of_expense: str, expense_amount: float, expense_category: str, employee_id: int) -> None:
        # expense
        expense = Expense(date_of_expense, expense_amount, expense_category, employee_id)

        for key, value in self.expenses.items():
            for e in self.employees_readin:
                if key == e.department_name and e.employee_id == employee_id:
                    value.append(expense)
                    print("The expense is successfully added!")

    def monthly_expense_report(self, department: str, month: str) -> None:
        # expense (month, expenses, employee ID), employee (employee ID, department)
        MyDict = {}
        for key, value in self.expenses.items():
            if key == department:
                for v in value:
                    if v.date_of_expense == month:
                        if v.employee_id not in MyDict.keys():
                            MyDict[v.employee_id] = v.expense_amount
                        else:
                            MyDict[v.employee_id] += v.expense_amount
        
        # print(MyDict)
        if not MyDict:
            print("There is no expense!")
        else:
            for key, value in MyDict.items():
                for e in self.employees_readin:
                    if key == e.employee_id:
                        print(f"first_name = {e.first_name}, last_name = {e.last_name}, total_expense = {value}")


    def monthly_summary_report(self, month: str) -> None:
        # expense (month, expenses, expense category, employee ID ), employee (employee ID, department)
        DepartmentExpenseDict = {}
        for key, value in self.expenses.items():
            MyDict = {}
            for v in value:
                if v.date_of_expense == month:
                    if v.expense_category not in MyDict.keys():
                        MyDict[v.expense_category] = v.expense_amount
                    else:
                        MyDict[v.expense_category] += v.expense_amount
            if MyDict:
                DepartmentExpenseDict[key] = MyDict
        
        if not DepartmentExpenseDict:
            print("There is no expense!")
        else:
            for key1, value1 in DepartmentExpenseDict.items():
                for key, value in value1.items():
                    print(f"department = {key1}, expense_category = {key}, total_expense = {value}")

    def monthly_expense_for_specified_category(self, category: str) -> None:
        # expense (month, expenses, expense category, employee ID ), employee (employee ID, department)
        for key, value in self.expenses.items():
            MyDict = {}
            for v in value:
                if v.expense_category == category:
                    if v.date_of_expense not in MyDict.keys():
                        MyDict[v.date_of_expense] = v.expense_amount
                    else:
                        MyDict[v.date_of_expense] += v.expense_amount

            if MyDict is None:
                print("There is no expense!")
            else:
                for key1, value1 in MyDict.items():
                    print(f"department = {key}, month = {key1}, total_expense = {value1}")

    def highest_expense_employee(self, month:str) -> None:
        # expense (month, expenses, expense category, employee ID ), employee (employee ID, department)
        MyDict = {}
        for key, value in self.expenses.items():
            for v in value:
                if v.date_of_expense == month:
                    if v.employee_id not in MyDict.keys():
                        MyDict[v.employee_id] = v.expense_amount
                    else:
                        MyDict[v.employee_id] += v.expense_amount
        # print(MyDict)
        
        max_key = 0
        max_value = 0
        for key, value in MyDict.items():
            if value > max_value:
                max_key = key
                max_value = value

        for d in self.departments:
            for e in d.employees:
                if max_key == e.employee_id:
                    print(f"{e}, total_expense = {max_value}")

    def department_over_budget_limit(self, month: str) -> None:
        # expense (month, expenses, expense category, employee ID ), employee (employee ID, department)
        # department_budget (department, budget)
        ExpenseDict = {}
        BudgetDict = {}
        if month == '2022-09-01':
            for d in self.departments:
                for key, value in d.department_budgets.items():
                    if d.name not in BudgetDict.keys():
                        BudgetDict[d.name] = value
                    else:
                        BudgetDict[d.name] += value
        else:
            self.read_old_department_budget_to_list()
            for budget in self.__old_department_budgets_readin:
                if budget.department_name not in BudgetDict.keys():
                    BudgetDict[budget.department_name] = budget.budget
                else:
                    BudgetDict[budget.department_name] += budget.budget

        # print(BudgetDict)

        for key, value in self.expenses.items():
            for v in value:
                if v.date_of_expense == month:
                    if key not in ExpenseDict.keys():
                        ExpenseDict[key] = v.expense_amount
                    else:
                        ExpenseDict[key] += v.expense_amount
        
        # print(ExpenseDict)

        if not ExpenseDict:
            print("There is no such department!")
        else: 
            for key, value in BudgetDict.items():
                for key1, value1 in ExpenseDict.items():
                    if key == key1 and value1 > value:
                        print(f"deparment = {key}, budget = {value}, total_expense = {value1}")

    def highest_expense_department(self, month: str) -> None:
        # expense, employee
        ExpenseDict = {}
        for key, value in self.expenses.items():
            for v in value:
                if v.date_of_expense == month:
                    if key not in ExpenseDict.keys():
                        ExpenseDict[key] = v.expense_amount
                    else:
                        ExpenseDict[key] += v.expense_amount
        
        # print(ExpenseDict)
        
        max_department = ''
        max_expense = 0
        for key, value in ExpenseDict.items():
            if value > max_expense:
                max_expense = value
                max_department = key
        
        print(f"department = {max_department}, total_expense = {max_expense}")

    def alerts_exceeding_budget_limit(self, sysdate = '2022-09-01') -> None:
        # expense, employee, department_budget

        ExpenseDict = {}
        BudgetDict = {}
        for d in self.departments:
            for key, value in d.department_budgets.items():
                if d.name not in BudgetDict.keys():
                    BudgetDict[d.name] = value
                else:
                    BudgetDict[d.name] += value

        # print(BudgetDict)

        for key, value in self.expenses.items():
            for v in value:
                if v.date_of_expense == sysdate:
                    if key not in ExpenseDict.keys():
                        ExpenseDict[key] = v.expense_amount
                    else:
                        ExpenseDict[key] += v.expense_amount
        
        # print(ExpenseDict)

        found = False
        for key, value in BudgetDict.items():
            for key1, value1 in ExpenseDict.items():
                if key == key1 and value1 >= value * 0.9 and value1 <= value:
                    found = True
                    print(f"{key} department has a total expense of {value1}, close to its budget {value}!")
        if found == False:
            print("There is no such department!")

    def total_counts_of_expense_category_histogram(self, department: str, month: str):
        # expense, employee
        lst = {}
        for key, value in self.expenses.items():
            if key == department:
                for v in value:
                    if v.date_of_expense == month:
                        if v.expense_category not in lst.keys():
                            lst[v.expense_category] = 1
                        else:
                            lst[v.expense_category] += 1

        # print(lst)

        max = 0
        for key, value in lst.items():
            if value >= max:
                max = value
        
        title = ''
        for key, value in lst.items():
            title += str(value) + (' ')*(len(key))
        print(title)
        
        for i in range(max):
            eval = max - i
            output = ''
            for key, value in lst.items():
                if value >= eval:
                    output += '*' + (' ')*(len(key))
                if value < eval:
                    output += (' ')*(len(key) + 1)
            print(output)
        
        label = ''
        for key, value in lst.items():
            label += f'{key}' + ' '
        print(label)

    def department_total_monthly_expense_histogram(self, month: str):
        # expense, employee
        lst = {}

        for key, value in self.expenses.items():
            for v in value:
                if v.date_of_expense == month:
                    if key not in lst.keys():
                        lst[key] = v.expense_amount
                    else:
                        lst[key] += v.expense_amount

        # print(lst)

        max = 0
        for key, value in lst.items():
            if value/1000 >= max:
                max = value/1000
        
        title = ''
        for key, value in lst.items():
            title += str(int(value)) + (' ')*(len(key) + 1 - len(str(int(value))))
        print(title)
        
        for i in range(int(max)):
            eval = max - i
            output = ''
            for key, value in lst.items():
                if value/1000 >= eval:
                    output += '*' + (' ')*(len(key))
                if value/1000 < eval:
                    output += (' ')*(len(key) + 1)
            print(output)
        
        label = ''
        for key, value in lst.items():
            label += f'{key}' + ' '
        print(label)

    def employee_total_monthly_expense_histogram(self, month: str):
        # expense
        lst = {}

        for key, value in self.expenses.items():
                for v in value:
                    if v.date_of_expense == month:
                        if v.employee_id not in lst.keys():
                            lst[v.employee_id] = v.expense_amount
                        else:
                            lst[v.employee_id] += v.expense_amount

        lst1 = {}
        for d in self.departments:
            for e in d.employees:
                for key, value in lst.items():
                    if e.employee_id == key:
                        name = e.first_name + ' ' + e.last_name
                        if name not in lst1.keys():
                            lst1[name] = value

        # print(lst1)

        max = 0
        for key, value in lst1.items():
            if value/1000 >= max:
                max = value/1000
        
        title = ''
        for key, value in lst1.items():
            title += str(int(value)) + (' ')*(len(key) + 1 - len(str(int(value))))
        print(title)
        
        for i in range(int(max)):
            eval = max - i
            output = ''
            for key, value in lst1.items():
                if value/1000 >= eval:
                    output += '*' + (' ')*(len(key))
                if value/1000 < eval:
                    output += (' ')*(len(key) + 1)
            print(output)
        
        label = ''
        for key, value in lst1.items():
            label += f'{key}' + ' '
        print(label)

    def modify_budget_for_one_category(self, category: str, percentage: float) -> None:
        # department_budget
        # first save the old budget to a csv file
        DBRepoOld = DepartmentBudgetRepositoryOld()
        old_lst = []
        for d in self.departments:
            for key, value in d.department_budgets.items():
                db = Department_Budget(d.name, key, value)
                old_lst.append(db)
        DBRepoOld.write_department_budgets(old_lst)
        
        found = False
        for d in self.departments:
            for key, value in d.department_budgets.items():
                if key == category:
                    found = True
                    d.department_budgets[key] = value * (1 - percentage)

        if found == True:
            print("The budget is successfully modified!")

    def modify_budget_for_all_category(self, percentage: float):
        # department_budget
                # first save the old budget to a csv file
        DBRepoOld = DepartmentBudgetRepositoryOld()
        old_lst = []
        for d in self.departments:
            for key, value in d.department_budgets.items():
                db = Department_Budget(d.name, key, value)
                old_lst.append(db)
        DBRepoOld.write_department_budgets(old_lst)
        
        for d in self.departments:
            for key, value in d.department_budgets.items():
                    d.department_budgets[key] = value * (1 - percentage)
        
        print("The budget is successfully modified!")
                                                                                                  
    def percentage_used_for_department_category(self, month: str) -> None:
        # show the percentage of budget of each expense category for each department for a specified month
        budgetDict = {}
        expenseDict = {}
        
        for d in self.departments:
            if d.name not in budgetDict.keys():
                budgetDict[d.name] = d.department_budgets
            else:
                budgetDict[d.name].update(d.department_budgets)

        # print(budgetDict)

        for key, value in self.expenses.items():
            for v in value:
                if v.date_of_expense == month:
                    if key not in expenseDict.keys():
                        item = {}
                        if v.expense_category not in item.keys():
                            item[v.expense_category] = v.expense_amount
                        else:
                            item[v.expense_category] += v.expense_amount
                        expenseDict[key] = item
                    else:
                        if v.expense_category not in expenseDict[key].keys():
                            expenseDict[key][v.expense_category] = v.expense_amount
                        else:
                            expenseDict[key][v.expense_category] += v.expense_amount

        # print(expenseDict)
       
        for key, value in budgetDict.items():
            for v_key, v_value in value.items():
                for key1, value1 in expenseDict.items():
                    for v1_key, v1_value in value1.items():
                        if key == key1 and v_key == v1_key:
                            percentage = v1_value/v_value
                            print(f"department = {key}, expense_category = {v_key}, budget = {v_value}, total_expense = {v1_value}, percentage_of_budget_used = {percentage:.2%}")
        
    def display_employee_expense_by_id(self) -> None:
        lst = {}
        for key, value in self.expenses.items():
            for v in value:
                if v.employee_id not in lst.keys():
                    lst[v.employee_id] = [v]
                else:
                    lst[v.employee_id].append(v)
        lst = dict(sorted(lst.items()))
        
        for key, value in lst.items():
            for v in value:
                print(v)


def main():
    tracker = Expense_Tracker('CFO')
    tracker.read_department_budget_to_list()
    tracker.read_employees_to_list()
    tracker.read_expenses_to_list()
    tracker.create_department_list()
    tracker.create_expense_list()

    # for d in tracker.departments:
    #     print(d.name)
    #     for e in d.employees:
    #         print(e)
    # print("=======================================================")

    # for department_budget in tracker.department_budgets_readin:
    #     print(department_budget)
    # print("=======================================================")
    
    # for e in tracker.employees_readin:
    #     print(e)
    # print("=======================================================")

    # for expense in tracker.expenses_readin:
    #     print(expense)
    # print("=======================================================")

    # tracker.add_employee(22, 'Allison', 'Ding', 'Sales', 'Senior Manager')
    # for d in tracker.departments:
    #     for e in d.employees:
    #         print(e)
    # print("=======================================================")

    # tracker.modify_employee(22, 'Allison', 'Deng', 'Marketing', 'Staff')
    # for d in tracker.departments:
    #     for e in d.employees:
    #         print(e)
    # for d in tracker.departments:
    #     print(d.employees)
    # print("=======================================================")

    # tracker.find_employee(22)
    # print("=======================================================")

    # tracker.remove_employee(22)
    # tracker.remove_employee(22)
    # print("=======================================================")

    # tracker.add_department('Sanctions')
    # for d in tracker.departments:
    #     print(d.name)
    # print("=======================================================")

    # tracker.find_department('Marketing')
    # print("=======================================================")

    # tracker.modify_department('Marketing', 'Market')
    # for d in tracker.departments:
    #     print(d)

    # tracker.modify_department('Market', 'Marketing')
    # for d in tracker.departments:
    #     print(d.name)
    # print("=======================================================")
    
    # for key, value in tracker.expenses.items():
    #     for v in value:
    #         print(key, v)
    # print("=======================================================")
     
    # tracker.input_expense('2022-01-01', 330, 'Equipment', 1)
    # for key, value in tracker.expenses.items():
    #     for v in value:
    #         print(f"department = {key}, expense = {v}")
    # print("=======================================================")
    
    # tracker.monthly_expense_report('Sales', '2022-08-01')
    # print("=======================================================")
    
    # tracker.monthly_summary_report('2022-08-01')
    # print("=======================================================")
    
    # tracker.monthly_expense_for_specified_category('Transportation')
    # print("=======================================================")
    
    # tracker.highest_expense_employee('2022-08-01')
    # print("=======================================================")

    # tracker.department_over_budget_limit('2022-09-01')
    # print("=======================================================")
 
    # tracker.highest_expense_department('2022-08-01')
    # print("=======================================================")
    
    tracker.alerts_exceeding_budget_limit('2022-09-01')
    print("=======================================================")

    # tracker.total_counts_of_expense_category_histogram('Engineering', '2022-01-01')
    # print()
    # tracker.total_counts_of_expense_category_histogram('Sales', '2022-08-01')
    # print("=======================================================")

    # tracker.department_total_monthly_expense_histogram('2022-08-01')
    # print("=======================================================")

    # tracker.employee_total_monthly_expense_histogram('2022-09-01')
    # print("=======================================================")

    # tracker.modify_budget_for_one_category('Transportation', 0.1)
    # for d in tracker.departments:
    #     for key, value in d.department_budgets.items():
    #         print(f"department = {d.name}, category = {key}, budget = {value}")
    # print("=======================================================")

    # tracker.modify_budget_for_all_category(0.1)
    # for d in tracker.departments:
    #     for key, value in d.department_budgets.items():
    #         print(f"department = {d.name}, category = {key}, budget = {value}")
    # print("=======================================================")
    
    # tracker.percentage_used_for_department_category('2022-08-01') 
    # print("=======================================================")
    
    # tracker.display_employee_expense_by_id()
    # print("=======================================================")
    
    # tracker.save_employees_to_csv() 
    # print("=======================================================")
 
    # tracker.save_expenses_to_csv()
    # print("=======================================================")

    # tracker.save_department_budgets_to_csv()

main()