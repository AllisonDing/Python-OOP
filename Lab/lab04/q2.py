class Room:
    def __init__(self, type: str, size: int) -> None:
        self.__type = type # e.g. Bedroom, den, storeroom
        if size < 0:
            raise ValueError("The Room size cannot be negative!")
        self.__size = size # e.g. squarefeet
    
    @property
    def type(self) -> str:
        return self.__type
    
    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int) -> None:
        if size < 0:
            raise ValueError("The Room size cannot be negative!")
        self.__size = size
    
    def __str__(self) -> str:
        return f"Room type = {self.__type}, size = {self.__size}"

    def __repr__(self) -> str:
        return str(self)

class Garage:
    def __init__(self, type: str, size: int, door_type: str) -> None:
        self.__type = type #e.g. single or double
        if size < 0:
            raise ValueError("The Garage size cannot be negative!")
        self.__size = size #e.g. squarefeet
        self.__door_type = door_type #e.g. auto or manual
    
    @property
    def type(self) -> str:
        return self.__type
    
    @property
    def size(self) -> int:
        return self.__size
    
    @property
    def door_type(self) -> str:
        return self.__door_type

    @size.setter
    def size(self, size: int) -> None:
        if size < 0:
            raise ValueError("The Garage size cannot be negative!")
        self.__size = size

    def __str__(self) -> str:
        return f"Garage type = {self.__type}, size = {self.__size} square feet, door_type = {self.__door_type}"
    
class Television:
    def __init__(self, screen_type: str, screen_size: int, resolution: str, price: float) -> None:
        self.__screen_type = screen_type #e.g. LCD, OLED, etc.
        self.__screen_size = screen_size #e.g. 65 inches
        self.__resolution = resolution # e.g. 1080p, 4K
        self.__price = price
    
    @property
    def screen_type(self) -> str:
        return self.__screen_type
    
    @property
    def screen_size(self) -> int:
        return self.__screen_size
    
    @property
    def resolution(self) -> str:
        return self.__resolution
    
    @property
    def price(self) -> float:
        return self.__price

    def __str__(self) -> str:
        return f"Television screen type = {self.__screen_type}, screen size = {self.__screen_size} inches, resolution = {self.__resolution}, price = {self.__price}"

    def __repr__(self) -> str:
        return str(self)

class House:
    def __init__(self, address: str, square_feet: int, garage: Garage) -> None:
        self.__address = address
        self.__square_feet = square_feet
        self.__rooms: list[Room] = []
        self.__garage = garage
        self.__televisions: list[Television] = []
    
    def add_room(self, room:Room) -> None:
        # add room to the house
        new_room = Room(room.type, room.size)
        self.__rooms.append(new_room)

    def add_tv(self, tv: Television) -> None:
        # add television to the house
        self.__televisions.append(tv)

    def remove_tv(self, tv: Television) -> list[Television]:
        # remove television from the house
        for i in self.__televisions:
            if i.screen_type == tv.screen_type and i.screen_size == tv.screen_size and i.resolution == tv.resolution and i.price == i.price:
                self.__televisions.remove(i)
        return self.__televisions

    def change_garage_size(self, size: int) -> Garage:
        # change garage size
        self.__garage.size = size
        return self.__garage
    
    def get_biggest_room(self) -> Room:
        # get the largest room
        MyDict = {}
        for room in self.__rooms:
            MyDict[room] = room.size
        
        return max(MyDict, key=lambda room:MyDict[room])

    def get_oled_televisions(self) -> list[Television]:
        # get all the OLED televisions
        list = []
        for tv in self.__televisions:
            if tv.screen_type.lower() == 'oled':
                list.append(tv)
        return list

    def is_similar_house(self, other) -> bool:
        # test if two houses are similar
        # if two houses have the same square feet and same number of rooms they are similar
        if self.__square_feet == other.__square_feet and len(self.__rooms) == len(other.__rooms):
            return True
        else:
            return False

    def __str__(self) -> str:
        return f"House address = {self.__address}, square feet = {self.__square_feet} , rooms = {self.__rooms}, garage = {self.__garage}, televisions = {self.__televisions}"

def main():
    # House A address
    address = "826 Paradise Drive"
    # House A garage
    garage = Garage("single", 250, "auto")
    
    # initiate House A
    House_A = House(address, 2550, garage)

    # add 4 rooms to House A
    room1 = Room("den", 200)
    room2 = Room("Bedroom", 123)
    room3 = Room("storeroom", 234)
    room4 = Room("restroom", 333)
    
    House_A.add_room(room1)
    House_A.add_room(room2)
    House_A.add_room(room3)
    House_A.add_room(room4)

    # add 3 televisions to House A
    tv1 = Television("LCD", 65, "1080p", 299.99)
    tv2 = Television("OLED", 74, "4K", 999.99)
    tv3 = Television("OLED", 65, "4K", 1299.99)
 
    House_A.add_tv(tv1)
    House_A.add_tv(tv2)
    House_A.add_tv(tv3)
    print(House_A)

    # remove one television from House A
    tv_removal = Television("OLED", 65, "4K", 1299.99)
    House_A.remove_tv(tv_removal)
    print(House_A)
    
    # change garage object's size
    House_A.change_garage_size(150)
    print(House_A)

    # get biggest room
    biggest_room = House_A.get_biggest_room()
    print(biggest_room)

    # get OLED televisions
    oled_televisions = House_A.get_oled_televisions()
    print(oled_televisions)

    # create House B and House C and House D
    # House B has same square feet and same number of rooms with House A
    # House C has same square feet but different number of rooms with House B
    # House D has different square feet but same number of rooms with House C
    address_b = "825 Paradise Drive"
    garage_b = Garage("single", 250, "auto")
    House_B = House(address_b, 2550, garage_b)
    room1_b = Room("den", 24)
    room2_b = Room("Bedroom", 28)
    room3_b = Room("storeroom", 30)
    room4_b = Room("restroom", 33)
    
    House_B.add_room(room1_b)
    House_B.add_room(room2_b)
    House_B.add_room(room3_b)
    House_B.add_room(room4_b)

    address_c = "824 Paradise Drive"
    garage_c = Garage("single", 250, "auto")
    House_C = House(address_c, 2550, garage_c)
    room1_c = Room("den", 24)
    room2_c = Room("Bedroom", 28)
    room3_c = Room("storeroom", 30)
    
    House_C.add_room(room1_c)
    House_C.add_room(room2_c)
    House_C.add_room(room3_c)

    address_d = "825 Paradise Drive"
    garage_d = Garage("single", 250, "auto")
    House_D = House(address_d, 250, garage_d)
    room1_d = Room("den", 24)
    room2_d = Room("Bedroom", 28)
    room3_d = Room("storeroom", 30)
    room4_d = Room("restroom", 33)
    
    House_D.add_room(room1_d)
    House_D.add_room(room2_d)
    House_D.add_room(room3_d)
    House_D.add_room(room4_d)

    print("House A and House B are similar: ", House_A.is_similar_house(House_B))
    print("House A and House C are similar: ", House_A.is_similar_house(House_C))
    print("House A and House D are similar: ", House_A.is_similar_house(House_D))

if __name__ == "__main__":
    main()

    
    



