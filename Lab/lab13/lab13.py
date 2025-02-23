from abc import ABC, abstractmethod

class Book:
    def __init__(self, isbn: str, title: str, author: str = "", price: float = 0.0) -> None:
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__price = price

    @property
    def isbn(self) -> str:
        return self.__isbn

    @property
    def title(self) -> str:
        return self.__title

    @property
    def author(self) -> str:
        return self.__author
    
    @property
    def price(self) -> float:
        return self.__price

    def __str__(self) -> str:
        output = f"Book isbn={self.__isbn}, title={self.__title}, author = {self.__author}, price = {self.__price}"
        return output
    
class BookList:
    def __init__(self) -> None:
        self.__books: list[Book] = []
    
    @property
    def books(self) -> list[Book]:
        return self.__books

    def add_book(self, book: Book):
        if book not in self.__books:
            self.__books.append(book)
    
    def __str__(self) -> str:
        output = ""
        for book in self.__books:
            output += str(book) + "\n"
        return output

class OrderItem:
    def __init__(self, isbn: str, quantity: int) -> None:
        self.__isbn = isbn
        self.__quantity = quantity

    @property
    def isbn(self) -> str:
        return self.__isbn
    
    @property
    def quantity(self) -> int:
        return self.__quantity
    
    def __str__(self) -> str:
        output = f"ibsn = {self.__isbn}, quantity = {self.__quantity}"
        return output

class Order:
    def __init__(self) -> None:
        self.__order_items: list[OrderItem] = []

    @property
    def order_items(self) -> list[OrderItem]:
        return self.__order_items

    def add_item(self, isbn, quantity):
        self.__order_items.append(OrderItem(isbn, quantity))
    
    def __str__(self) -> str:
        output = ""
        for item in self.__order_items:
            output += str(item) + '\n'
        return output

class Invoice:
    def __init__(self, order: Order, book_list: BookList) -> None:
        self.__order = order
        self.__book_list = book_list
    
    @property
    def order(self) -> Order:
        return self.__order
    
    @property
    def book_list(self) -> BookList:
        return self.__book_list
    
    def invoice_total(self) -> float:
        total = 0
        for item in self.__order.order_items:
            for book in self.__book_list.books:
                if item.isbn == book.isbn:
                    total += item.quantity * book.price
        return total

    def __str__(self) -> str:
        print("===========invoice===========")
        print("This order details are: ")
        output = ''
        for item in self.__order.order_items:
            for book in self.__book_list.books:
                if item.isbn == book.isbn:
                    output += f"order item: {item}\nbook: {book}\n"
        output += f"This order total cost is: {self.invoice_total()}\n"
        return output


###########################################################################################
class Command(ABC):
    @abstractmethod
    def execute(self) -> str:
        pass

class DisplayBookListCommand(Command):
    def __init__(self, book_list: BookList) -> None:
        self.__book_list = book_list

    def execute(self) -> str:
        return str(self.__book_list)

class AddOrderItemCommand(Command):
    def __init__(self, order: Order) -> None:
        self.__order = order

    def execute(self) -> str:
        isbn = input("Enter isbn: ")
        quantity = int(input("Enter quantity: "))
        self.__order.add_item(isbn, quantity)
        return str(self.__order)

class DisplayInvoiceCommand(Command):
    def __init__(self, invoice: Invoice) -> None:
        self.__invoice = invoice

    def execute(self) -> str:
        return str(self.__invoice)

class Invoker:
    def __init__(self) -> None:
        self.__commands = []

    def add_command(self, command):
        self.__commands.append(command)

    def execute_command(self, command_no) -> str:
        return self.__commands[command_no-1].execute()

############################################################################################
class BookApplication:
    def __init__(self) -> None:
        self.__order = Order()
        self.__invoker = Invoker()
        self.__booklist = BookList()
        self.__booklist.add_book(Book("111", "C++", "Ken Cheung", 13.20))
        self.__booklist.add_book(Book("222", "Java", "Jonathan Robert", 25.99))

    @property
    def order(self):
        return self.__order

    @property
    def booklist(self):
        return self.__booklist

    def add_command(self, command):
        self.__invoker.add_command(command)


    def show_menu(self):
        print("\n======== Menu  ============")
        print("1. Display Book List")
        print("2. Add Order Item")
        print("3. Display Invoice")
        print("4. Exit")

    def process_command(self, command_no):
        print(self.__invoker.execute_command(command_no))

def main():
    app = BookApplication()
    app.add_command(DisplayBookListCommand(app.booklist))
    app.add_command(AddOrderItemCommand(app.order))
    app.add_command(DisplayInvoiceCommand(Invoice(app.order, app.booklist)))


    while True:
        app.show_menu()
        command_no = int(input("Please enter a command no: "))
        if command_no == 4:
            break
        elif command_no < 4:
            app.process_command(command_no)
        else:
            print("This command does not exist!")

if __name__ == "__main__":
    main()




