from expense import Expense

class Employee:
    def __init__(self, employee_id: int, first_name: str, last_name: str, department_name: str, rank: str) -> None:
        self.__employee_id = employee_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__department_name = department_name
        self.__rank = rank
        self.__expenses: list[Expense] = []

    @property
    def employee_id(self) -> int:
        return self.__employee_id
    
    @property
    def first_name(self) -> str:
        return self.__first_name
    
    @first_name.setter
    def first_name(self, first_name: str) -> None:
        self.__first_name = first_name
    
    @property
    def last_name(self) -> str:
        return self.__last_name
    
    @last_name.setter
    def last_name(self, last_name: str) -> None:
        self.__last_name = last_name
    
    @property
    def department_name(self) -> str:
        return self.__department_name
    
    @department_name.setter
    def department_name(self, department_name: str) -> None:
        self.__department_name = department_name
    
    @property
    def rank(self) -> str:
        return self.__rank
    
    @rank.setter
    def rank(self, rank: str) -> None:
        self.__rank = rank
    
    @property
    def expenses(self) -> list[Expense]:
        return self.__expenses

    def get_csv(self) -> list[str]:
        csv_str: list[str] = [str(self.employee_id), self.first_name, self.last_name, self.department_name, self.rank]
        return csv_str
    
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Employee):
            return __o.employee_id == self.employee_id
        else:
            return False

    def __str__(self) -> str:
        output = f"employee_id = {self.__employee_id}, first_name = {self.__first_name}, last_name = {self.__last_name}, department_name = {self.__department_name}, rank = {self.__rank}"
        return output

    def __repr__(self) -> str:
        return str(self)


    
 