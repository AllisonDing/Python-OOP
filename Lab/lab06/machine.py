from abc import ABC, abstractmethod, abstractproperty

class Movable(ABC): #create Abstract class Movable
    @abstractmethod #create abstract method move
    def move(self) -> None:
        pass

class Displayable(ABC): #create Abstract class Displayable
    @abstractmethod #create abstract method display
    def display(self) -> None:
        pass

class Flyable(ABC): #create Abstract class Flyable
    @abstractmethod #create abstract method fly
    def fly(self) -> None:
        pass

class Part(Displayable): #subclass Part
    def __init__(self, partno: int, price: float) -> None:
        self.__partno = partno
        self.__price = price

    @property
    def partno(self) -> int:
        return self.__partno

    @property
    def price(self) -> float:
        return self.__price

    def display(self) -> None: #abstract method inherited
        output = f"partno = {self.__partno}\nprice = {self.__price}"
        print(output)

class Machine(Displayable): #subclass Machine, which is also an abstract class
    def __init__(self, machine_name: str) -> None:
        self.__machine_name = machine_name
        self.__parts: list[Part] = []

    @property
    def machine_name(self) -> str:
        return self.__machine_name

    def get_parts(self) -> list[Part]: #function to get parts
        return self.__parts

    @abstractmethod #create abstract method
    def dowork(self) -> None:
        pass

    def add_part(self, part: Part) -> None:
        self.__parts.append(part)

    def display(self) -> None: #abstract method inherited
        print(f"machine_name = {self.__machine_name}")
        print(f"The machine has these parts:")
        for p in self.__parts:
            p.display()
            print()

    def remove_part(self, partno: int) -> None:
        for part in self.__parts:
            if part.partno == partno:
                self.__parts.remove(part)

    def remove_part1(self, partno: int) -> None:
        target_part = Part(partno, 0)
        self.__parts.remove(target_part)

    def find_duplicated_parts(self) -> dict[int, int]:
        duplicated_parts: dict[int, int] = {}
        for part in self.__parts:
            if part.partno in duplicated_parts:
                duplicated_parts[part.partno] += 1
            else:
                duplicated_parts[part.partno] = 1

        return {k: v for k, v in duplicated_parts.items() if v > 1} #freq > 1

    def getMovableParts(self) -> list[Part]:
        MovableParts: list[Part] = []
        for p in self.__parts:
            if isinstance(p, Movable):
                MovableParts.append(p)

        return MovableParts
    
    def __iter__(self):
        self.__index = -1
        return self
    
    def __next__(self):
        if self.__index >= len(self.__parts) - 1:
            raise StopIteration()
        self.__index += 1
        part = self.__parts[self.__index]
        return part


class MovablePart(Movable, Part): #create subclass
    def __init__(self, partno: int, price: float, type: str) -> None:
        Part.__init__(self, partno, price)
        self.__type = type

    @property
    def type(self) -> str:
        return self.__type

    def display(self) -> None: #abstract method inherited
        Part.display(self)
        output = f"type = {self.__type}"
        print(output)

    def move(self) -> None: #abstract method inherited
        print(f"partno: {self.partno} is moving fast!")

class JetFighter(Displayable, Flyable): #create subclass 
    def __init__(self, model: str, speed: int) -> None:
        self.__model = model
        self.__speed = speed
    
    @property
    def model(self) -> str:
        return self.__model

    @property
    def speed(self) -> int:
        return self.__speed

    def fly(self) -> None: #abstract method inherited
        print(f"The JetFighter {self.__model} is flying in the sky!")

    def display(self) -> None: #abstract method inherited
        output = f"model = {self.__model}\nspeed = {self.__speed}\n"
        print(output)

class Robot(Machine, JetFighter): #create subclass
    def __init__(self, machine_name: str, cpu: str, model: str, speed: int) -> None:
        Machine.__init__(self, machine_name) #inherited attributes
        JetFighter.__init__(self, model, speed) #inherited attributes
        self.__cpu = cpu

    @property
    def cpu(self) -> str:
        return self.__cpu

    def dowork(self) -> None: #subclass method inherited
        print(f"The Robot {self.machine_name} is assembling a big truck.")

    def fly(self) -> None: #subclass method inherited
        JetFighter.fly(self)
        print(f"The Robot {self.machine_name} is flying over the ocean!")

    def display(self) -> None: #subclass method inherited
        print(f"cpu = {self.__cpu}")
        Machine.display(self) 
        JetFighter.display(self)

    def get_expensive_parts(self, price_limit: int) -> list[Part]:
        expensive_parts: list[Part] = []
        for p in self:
            if p.price >= price_limit:
                expensive_parts.append(p)

        return expensive_parts

    def get_movable_parts_bytype(self) -> dict[str, list[Part]]:
        bytype: dict[str, list[Part]] = {}
        # movable_parts = Machine.getMovableParts(self) #method inherited
        for p in self:
            if isinstance(p, Movable):
                if p.type in bytype:
                    bytype[p.type].append(p)
                
                else:
                    new_list = []
                    new_list.append(p)
                    bytype[p.type] = new_list

        return bytype

    def get_movable_parts(self) -> list[Part]:  #method inherited
        return Machine.getMovableParts(self) 

def main():
    robo = Robot('MTX', 'M1X', 'F-16', 10000)
    robo.add_part(Part(111, 100))
    robo.add_part(Part(222, 200))
    robo.add_part(Part(333, 300))
    robo.add_part(Part(222, 300))
    robo.add_part(MovablePart(555, 300, "TypeA"))
    robo.add_part(Part(111, 100))
    robo.add_part(Part(111, 100))
    robo.add_part(MovablePart(777, 300, "TypeB"))
    robo.add_part(MovablePart(655, 300, "TypeA"))
    robo.add_part(MovablePart(755, 300, "TypeA"))
    robo.add_part(MovablePart(977, 300, "TypeB"))

    robo.display()
    print()

    print("\nRobot test flight----")
    robo.fly()

    print("\nRobot dowork() test ----")
    robo.dowork()

    print("\nDuplicated part list----")
    partfreq = robo.find_duplicated_parts()
    for partno in partfreq.keys():
        print(partno,'=>', partfreq[partno], 'times')

    print("\nExpensive part list----")
    expensive_parts = robo.get_expensive_parts(200)
    for part in expensive_parts:
        part.display()

    print("\nMovable part list----")
    movable_parts = robo.get_movable_parts_bytype()
    for type, parts in movable_parts.items():
        print("type =", type)
        for part in parts:
            part.display()
        print()

    print("\nAsk movable to move----")
    movable_parts = robo.get_movable_parts()
    for part in movable_parts:
        part.move()
   
    print("\nTest remove_part() ----")
    robo.remove_part(333)
    for part in robo.get_parts():
        if part.partno == 333:
            print('Found 333')
            break;

if __name__ == "__main__":
    main()





    



    

            