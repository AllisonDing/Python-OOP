from abc import ABC, abstractmethod, abstractproperty

class Displayable(ABC):
    @abstractmethod
    def display(self) -> None:
        pass

class AbstractCompany(ABC):
    def __init__(self, max_num_employees = 10) -> None:
        self.__max_num_employees = max_num_employees

    @property
    def max_num_employees(self) -> int:
        return self.__max_num_employees

    @abstractmethod
    def get_employee_name_list(self) -> list[str]:
        pass

class Employee(Displayable):
    def __init__(self, empId: int, name: str, salary: float, title: str) -> None:
        self.__empId = empId
        self.__name = name
        self.__salary = salary
        self.__title = title

    @property
    def empId(self) -> int:
        return self.__empId

    @property
    def name(self) -> str:
        return self.__name

    @property
    def salary(self) -> float:
        return self.__salary

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str) -> None:
        self.__title = title

    def display(self) -> None:
        print(self)

    def __str__(self):
        return f"empId = {self.__empId}\nname = {self.__name}\nsalary = {self.__salary}\ntitle = {self.__title}\n"

    def __repr__(self) ->str:
        return str(self)

class Company(Displayable, AbstractCompany):
    def __init__(self, max_num_employees: int, comp_name: str) -> None:
        AbstractCompany.__init__(self, max_num_employees)
        self.__comp_name = comp_name
        self.__employees: list[Employee] = []
    
    @property
    def comp_name(self) -> str:
        return self.__comp_name

    def add_employee(self, employee: Employee) -> None:
        if len(self.__employees) < self.max_num_employees:
            self.__employees.append(employee)
        else:
            raise ValueError("The maximum number of employees is 10!")
    
    def remove_employee(self, empid: int) -> None:
        for e in self.__employees:
            if e.empId == empid:
                self.__employees.remove(e)
    
    def update_employee_title(self, empid: int, title: str) -> None:
        for e in self.__employees:
            if e.empId == empid:
                e.title = title
    
    def remove_all_employees_by_title(self, title: str) -> None:
        employees_by_title: list[Employee] = []
        for e in self.__employees:
            if e.title == title:
                employees_by_title.append(e)

        for e in employees_by_title:
            self.__employees.remove(e)

    def get_employee_name_list(self) -> list[str]:
        employee_name_list: list[str] = []
        for e in self.__employees:
            employee_name_list.append(e.name)

        return employee_name_list

    def __iter__(self):
        self.__index = -1
        return self

    def __next__(self):
        if self.__index >= len(self.__employees) - 1:
            raise StopIteration()
        self.__index += 1
        employee = self.__employees[self.__index]
        return employee

    def display(self) -> None:
        output = f"comp_name = {self.__comp_name}\nemployees = {self.__employees}"
        print(output)
        
        

class StockBusiness(Displayable):
    def __init__(self, research_tool: str, commission_rate: float) -> None:
        self.__research_tool = research_tool
        self.__commission_rate = commission_rate

    @property
    def research_tool(self) -> str:
        return self.__research_tool

    @property
    def commission_rate(self) -> float:
        return self.__commission_rate

    def trade(self, stock_name: str, num_shares: int) -> None:
        output = "trading" + stock_name + str(num_shares) + "shares!"
        print(output)

    def display(self) -> None:
        output = f"research_tool = {self.__research_tool}\ncommission_rate = {self.__commission_rate}"
        print(output)

class TradingCompany(Company, StockBusiness):
    def __init__(self, max_num_employees: int, comp_name: str, product_type: str, num_of_offices: int, research_tool: str, commision_rate: float) -> None:
        Company.__init__(self, max_num_employees, comp_name)
        StockBusiness.__init__(self, research_tool, commision_rate)
        self.__product_type = product_type
        self.__num_of_offices = num_of_offices

    @property
    def product_type(self) -> str:
        return self.__product_type
    
    @property
    def num_of_offices(self) -> int:
        return self.num_of_offices

    def get_employees_high_salary(self, limit: float) -> list[Employee]:
        high_salary: list[Employee] = []
        for e in self:
            if e.salary > limit:
                high_salary.append(e)

        return high_salary

    def get_employees_by_title(self) -> dict[str, list[str]]:
        employees_by_title: dict[str, list[str]] = {}
        for e in self:
            if e.title in employees_by_title:
                employees_by_title[e.title].append(e.name)

            else:
                new_list = []
                new_list.append(e.name)
                employees_by_title[e.title] = new_list
        return employees_by_title

    def get_employee_name_list(self) -> list[str]:
        return Company.get_employee_name_list(self)

    def display(self) -> None:
        Company.display(self)
        StockBusiness.display(self)
        output = f"product_type = {self.__product_type}\nnum_of_offices = {self.__num_of_offices}"
        print(output)

    
def main():
    A = Employee(1, "Allison", 100, "Officer")
    B = Employee(2, "Anthony", 200, "Supervisor")
    C = Employee(3, "Harshit", 300, "Manager")

    Comp = TradingCompany(10, "ABC Stock Trading Company", "Stocks", 5, "Bloomberg", 0.3)
    Comp.add_employee(A)
    Comp.add_employee(B)
    Comp.add_employee(C)

    SB = StockBusiness("Bloomberg", 0.3)

    Comp.display()
    print()

    # get employee name list
    employee_name_list = Comp.get_employee_name_list()
    print(employee_name_list)
    print()

    employee_by_title = Comp.get_employees_by_title()
    print(employee_by_title)
    print()

    employee_high_salary = Comp.get_employees_high_salary(100)
    print(employee_high_salary)
    print()

    Comp.remove_employee(3)
    Comp.display()
    print()
    
    Comp.remove_all_employees_by_title('Officer')
    Comp.display()
    print()

    Comp.update_employee_title(2, 'Manager')
    Comp.display()
    print()


    #remove employee


if __name__ == "__main__":
    main()











