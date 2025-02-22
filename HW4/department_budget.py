class Department_Budget:
    def __init__(self, department_name: str, expense_category: str, budget: float) -> None:
        self.__department_name = department_name
        self.__expense_category = expense_category
        self.__budget = budget

    @property
    def department_name(self) -> str:
        return self.__department_name
    
    @property
    def expense_category(self) -> str:
        return self.__expense_category
    
    @property
    def budget(self) -> float:
        return self.__budget
    
    @budget.setter
    def budget(self, budget) -> None:
        self.__budget = budget

    def get_csv(self) -> list[str]:
        csv_str: list[str] = [self.__department_name, self.__expense_category, str(self.__budget)]
        return csv_str
    
    def __str__(self) -> str:
        output = f"department_name = {self.__department_name}, expense_category = {self.__expense_category}, budget = {self.__budget}"
        return output
    
    def __repr__(self) -> str:
        return str(self)





  