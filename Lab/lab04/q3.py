class Month:
    MyDict = {"January":0, "February":1, "March":2, "April":3, "May":4, "June":5, "July":6, "August":7, "September":8, "October":9, "November":10, "December":11}
        
    def __init__(self, month_string: str) -> None:
        self.__month_number = Month.MyDict[month_string]
        if self.__month_number < 0 or self.__month_number >= 12:
            raise ValueError("Invalid Month!")

    @property
    def month_number(self):
        return self.__month_number

    def __str__(self) -> str:
        return f"month_number = {self.__month_number}"


    def advance(self) -> None:
        # get the following month number
        if self.__month_number == 11:
            self.__month_number = 11 - self.__month_number
        else:
            self.__month_number += 1
    
    def prev(self) -> None:
        # get the previous month
        if self.__month_number == 0:
            self.__month_number = 11 - self.__month_number
        else:
            self.__month_number -= 1
    
    def display(self) -> str:
        # display the input month
        for key in Month.MyDict.keys():
            if self.__month_number == Month.MyDict[key]:
                return key

    def compare(self, m: str) -> int:
        # compare the input month with the object month
        # if the input month is greater than the object month return 1
        # if the input month is smalelr than the object month return -1
        # if the input month is equal to the object month return 0
        if self.__month_number > Month.MyDict[m]:
            return 1
        elif self.__month_number < Month.MyDict[m]:
            return -1
        else:
            return 0

def main():
    # object: month string = "December"
    a = Month("December")
    print(a)
    
    a.advance()
    a.advance()
    a.advance()
    print(a.display())

    a.prev()
    a.prev()
    print(a.display())

    # m object
    m = "February"
    print(a.compare(m))

if __name__ == "__main__":
    main()
    
    









    