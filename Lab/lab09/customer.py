class Customer:
    def __init__(self, first_name: str, last_name: str, account_number: int, account_balance: float) -> None:
        self.__first_name = first_name
        self.__last_name = last_name
        self.__account_number = account_number
        self.__account_balance = account_balance
    
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
    def account_number(self) -> int:
        return self.__account_number
    
    @account_number.setter
    def account_number(self, account_number: int) -> None:
        self.__account_number = account_number 
    
    @property
    def account_balance(self) -> float:
        return self.__account_balance
    
    @account_balance.setter
    def account_balance(self, account_balance: float) -> None:
        self.__account_balance = account_balance
    
    def __str__(self) -> str:
        output = f"first_name = {self.__first_name}, last_name = {self.__last_name}, account_number = {self.__account_number}, account_balance = {self.__account_balance}"
        return output
    
    def display(self) -> None:
        print(self)

    # def __repr__(self) -> str:
    #     return str(self)
    
    def get_csv(self) -> list[str]:
        csv_str: list[str] = [self.__first_name, self.__last_name, str(self.__account_number), str(self.__account_balance)]
        return csv_str
    
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Customer):
            return __o.__account_number == self.__account_number
        else:
            return False

 