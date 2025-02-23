class Customer:
    def __init__(self, name: str, address: str) -> None:
        self.__name = name
        self.__address = address

    @property 
    def name(self) -> str:
        return self.__name

    @property 
    def address(self) -> str:
        return self.__address

    def __str__(self) -> str:
        return f"Customer name = {self.__name}, address = {self.__address}"

class Product:
    def __init__(self, productid: int, product_name: str, price: float) -> None:
        self.__productid = productid
        self.__product_name = product_name
        self.__price = price
    
    def productid(self) -> int:
        return self.__productid

    def product_name(self) -> str:
        return self.__product_name

    def price(self) -> float:
        return self.__price

    def __str__(self) -> str:
        return f"Product productid = {self.__productid}, product name = {self.__product_name}, price = {self.__price}"

class OrderItem:
    def __init__(self, product: Product, quantity: int) -> None:
        self.__product = product
        # error message
        if quantity < 0:
            raise ValueError("The quantity cannot be a negative number!")
        self.__quantity = quantity
    
    @property
    def product(self) -> Product:
        return self.__product

    @property
    def quantity(self) -> int:
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity: int) -> None:
        # error message
        if quantity < 0:
            raise ValueError("The quantity cannot be a negative number!")
        self.__quantity = quantity

    @property
    def total(self) -> float:
        # total = price * quantity
        return self.__product.price * self.__quantity
    
    def __str__(self) -> str:
        return f"Order item: Product = {self.__product}, quantity = {self.__quantity}"
    
    def __repr__(self) -> str:
        return str(self)

class Order:
    def __init__(self, orderid: int, customer: Customer) -> None:
        self.__orderid = orderid
        self.__customer = customer
        self.__order_items: list[OrderItem] = []

    def add_item(self, product: Product, quantity: int) -> None:
        # Check if the product is in the order item list
        # if yes, update the quantity 
        # if no, append the new order item
        found = False
        for item in self.__order_items:
            if item.product.productid == product.productid:
                item.quantity += quantity
                found = True
                break
                # or you can use return
        if found is False:
            self.__order_items.append(OrderItem(product, quantity))
    
    def remove_item(self, product: Product, quantity: int) -> None:
        # Search the product with the specified productid and remove it
        for item in self.__order_items:
            if item.product.productid == product.productid:
                item.quantity -= quantity
                break

    def find_largest_item(self) -> OrderItem:
        # Find the order item with the largest value (price * quantity)
        MyDict = {}
        for item in self.__order_items:
            MyDict[item] = item.product.price() * item.quantity
        
        return max(MyDict, key=lambda item:MyDict[item])
    
    def get_total(self) -> float:
         # return total value of the order
         # each order sum = price * quantity
        sum = 0 
        for item in self.__order_items:
            sum += item.product.price() * item.quantity 
        return sum

    def get_discount_value(self, discount_rate: float) -> float:
        # return total value of the order * discount rate 
        return self.get_total() * (1-discount_rate)

    def __str__(self) -> str:
        return f"Order orderid = {self.__orderid}, Customer = {self.__customer}, items = {self.__order_items}"

def main():
    c = Customer("Peter", "Mission Blvd, Fremont")
    p1 = Product(1111, "Desk", 109.99)
    p2 = Product(2222, "Chair", 99.99)
    p3 = Product(3333, "Computer", 1109.99)
    
    order = Order(123, c)
    order.add_item(p1, 10)
    order.add_item(p2, 20)
    order.add_item(p3, 30)
    order.remove_item(p1, 5)
    order.remove_item(p2, 15)
    order.remove_item(p3, 25)
    
    print(order)
    
    largest_item = order.find_largest_item()
    print(largest_item)
    
    total = order.get_total()
    print(total)
    
    discount_value = order.get_discount_value(0.15)
    print(discount_value)
    

if __name__ == "__main__":
    main()