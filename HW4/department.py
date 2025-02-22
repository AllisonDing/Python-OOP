from employee import Employee
from department_budget import Department_Budget

class Department:
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__department_budgets = {}
        self.__employees: list[Employee] = []
    
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name) -> None:
        self.__name = name

    @property
    def department_budgets(self):
        return self.__department_budgets
        
    @property
    def employees(self) -> list[Employee]:
        return self.__employees
    
    # add department_budget to department

    # add employee to department

    def __str__(self) -> str:
        output = f"name = {self.__name}, department_budgets = {self.__department_budgets}, employees = {self.__employees}"
        return output
    
    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Department):
            return __o.name == self.name
        else:
            return False

    

    
    




    
 