class Expense:
    def __init__(self, date_of_expense: str, expense_amount: float, expense_category: str, employee_id: int) -> None:
        self.__date_of_expense = date_of_expense
        self.__expense_amount = expense_amount
        self.__expense_category = expense_category
        self.__employee_id = employee_id

    @property
    def date_of_expense(self) -> str:
        return self.__date_of_expense
    
    @property
    def expense_amount(self) -> float:
        return self.__expense_amount
    
    @property
    def expense_category(self) -> str:
        return self.__expense_category
    
    @property
    def employee_id(self) -> int:
        return self.__employee_id

    def get_csv(self) -> list[str]:
        csv_str: list[str] = [self.__date_of_expense, str(self.__expense_amount), str(self.__expense_category), str(self.__employee_id)]
        return csv_str
 
    def __str__(self) -> str:
        output = f"date_of_expense = {self.__date_of_expense}, expense_amount = {self.__expense_amount}, expense_category = {self.__expense_category}, employee_id = {self.__employee_id}"
        return output
    
    def __repr__(self) -> str:
        return str(self)
