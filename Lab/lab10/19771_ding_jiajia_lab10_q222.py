from abc import ABC, abstractmethod
from typing import Optional

class Displayable(ABC):
    @abstractmethod
    def display():
        pass

class House(Displayable):
    def __init__(self, address: str, squareFeet: int, numRooms: int, price: float):
        self.__address = address
        self.__squareFeet = squareFeet
        self.__numRooms = numRooms
        self.__price = price

    # add some public properties here if necessary 
    @property
    def address(self) -> str:
        return self.__address

    @property
    def price(self) -> float:
        return self.__price
    
    @price.setter
    def price(self, price: float) -> None:
        if price < 0:
            raise ValueError("The price cannot be a ngative number!")
        self.__price = price

    def __str__(self) -> str:
        return f"Address = {self.__address}, Square Feet = {self.__squareFeet}, Number of Rooms = {self.__numRooms}, Price = {self.__price}"

    def display(self):
        print(self)

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, House):
            return self.__address == __o.__address
        else:
            return False

class Contact(Displayable):
    def __init__(self, firstName, lastName, phoneNumber, email):
        self.__lastName = lastName
        self.__firstName = firstName
        self.__email = email
        self.__phoneNumber = phoneNumber

    @property
    def firstName(self):
        return self.__firstName
    
    @property
    def lastName(self):
        return self.__lastName

    # add some public properties here if necessary 
    def __str__(self) -> str:
        return f"Last Name = {self.__lastName}, First Name = {self.__firstName}, Phone Number = {self.__phoneNumber}, Email = {self.__email}"

    def display(self):
        print(self)
    
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Contact):
            return self.__email == __o.__email and self.__phoneNumber == __o.__phoneNumber
        else:
            return False

    @abstractmethod
    def notify_when_add():
        pass

    @abstractmethod
    def notify_when_remove():
        pass

    @abstractmethod
    def notify_when_edit():
        pass


class Owner(Contact):
    def __init__(self, lastName, firstName, phoneNumber, email):
        super().__init__(lastName, firstName, phoneNumber, email)
        self.__houses = []

    @property
    def houses(self):
        return self.__houses

    def addHouse(self, house):
        if house not in self.__houses:
            self.__houses.append(house)
        
    def display(self):
        super().display()
        print("Owns the following houses:")
        for h in self.__houses:
            h.display()
    #add notifications to owners
    def notify_when_add(self, house):
        for h in self.__houses:
            if h == house:
                print(f"Dear owner: {super().firstName} {super().lastName}, the following house of yours has been added:")
                h.display()
    #remove notifications to owners
    def notify_when_remove(self, house):
        for h in self.__houses:
            if h == house:
                print(f"Dear owner: {super().firstName} {super().lastName}, the following house of yours has been removed:")
                h.display()
    #edit notifications to owners
    def notify_when_edit(self, house):
        for h in self.__houses:
            if h == house:
                print(f"Dear owner: {super().firstName} {super().lastName}, the following house of yours has updated the price:")
                h.display()


class Buyer(Contact):
    def __init__(self, lastName, firstName, phoneNumber, email):
        super().__init__(lastName, firstName, phoneNumber, email)
        self.__watchList = []

    @property
    def watchList(self):
        return self.__watchList

    #  Save the house in his watch list 
    def saveForLater(self, house: House) -> None:
        if house not in self.__watchList:
            self.__watchList.append(house)
            #add notifications to buyers 
            self.notify_when_add(house) 

    # Remove the house from his watch list
    def removeFromSaveForLater(self, house: House):
        if house in self.__watchList:
            self.__watchList.remove(house)

    def display(self):
        super().display()
        print("Watching the following houses:")
        for h in self.__watchList:
            h.display()
    #add notifications to buyers
    def notify_when_add(self, house):
        print(f"Dear buyer: {super().firstName} {super().lastName}, the following house has been added:")
        house.display()
    #remove notifications to buyers
    def notify_when_remove(self, house):
        for h in self.watchList:
            if h == house:
                print(f"Dear buyer: {super().firstName} {super().lastName}, the following house has been removed:")
                h.display()
    #edit notifications to buyers
    def notify_when_edit(self, house):
        for h in self.watchList:
            if h == house:
                print(f"Dear buyer: {super().firstName} {super().lastName}, the following house has updated the price:")
                house.display()

class Company(Displayable):
    def __init__(self, companyName):
        self.__companyName = companyName
        self.__owners = []
        self.__buyers = []
        self.__agents = []
        self.__houses = []

    @property
    def owners(self):
        return self.__owners
    
    @property
    def buyers(self):
        return self.__buyers
    
    @property
    def agents(self):
        return self.__agents

    def addOwner(self, owner):
        if owner not in self.__owners:
            self.__owners.append(owner)

    def addBuyer(self, buyer):
        if buyer not in self.__buyers:
            self.__buyers.append(buyer)

    def addAgent(self, agent):
        if agent not in self.__agents:
            self.__agents.append(agent)

    def addHouseToListing(self, house):
        if house not in self.__houses:
            self.__houses.append(house)
        #add notification to the owners
        for o in self.__owners:
            o.notify_when_add(house)
        #add notification to the agents
        for a in self.__agents:
            a.notify_when_add(house)

    def getHouseByAddress(self, address: str) -> Optional[House]:
        house = House(address, 0, 0, 0)
        if house in self.__houses:
            idx = self.__houses.index(house)
            return self.__houses[idx]
        else:
            return None

    def removeHouseFromListing(self, house):
        if house in self.__houses:
            self.__houses.remove(house)
            #remove notifications to the owners
            for o in self.__owners:
                o.notify_when_remove(house)
            #remove notifications to the agents
            for a in self.__agents:
                a.notify_when_remove(house)

        else:
            print("We cannot find the house!")

    # Help to remove that house from all buyers' watch list.
    def removeHouseFromSaveForLater(self, house):
        for buyer in self.__buyers:
            #remove notifications to buyers
            buyer.notify_when_remove(house)
            buyer.removeFromSaveForLater(house)
            

    def getBuyersByHouse(self, house):
        for buyer in self.__buyers:
            for w in buyer.watchList:
                if w == house:
                    buyer.display()
    

    def display(self):
        print(f"Company Name = {self.__companyName}")
        print("=========================== The list of agents: ==============================")
        for agent in self.__agents:
            agent.display()
        print("=========================== The house listing: ==============================")
        for house in self.__houses:
            house.display()
        print("=========================== The list of owners: ==============================")
        for owner in self.__owners:
            owner.display()
        print("=========================== The list of buyers: ==============================")
        for buyer in self.__buyers:
            buyer.display()
        

class Agent(Contact):
    def __init__(self, lastName, firstName, phoneNumber, email, position, company: Company):
        super().__init__(lastName, firstName, phoneNumber, email)
        self.__position = position
        self.__company = company

    def addHouseToListingForOwner(self, owner, house):
        self.__company.addOwner(owner)
        self.__company.addHouseToListing(house)

    def helpBuyerToSaveForLater(self, buyer: Buyer, house): 
        self.__company.addBuyer(buyer)
        buyer.saveForLater(house)

    def editHousePrice(self, address, newPrice: int):
        h = self.__company.getHouseByAddress(address)
        print()
        if h != None:
            h.price = newPrice
            #edit notifications to owners
            for o in self.__company.owners:
                o.notify_when_edit(h)
            #edit notifications to agents
            for a in self.__company.agents:
                a.notify_when_edit(h)
            #edit notifications to buyers
            for b in self.__company.buyers:
                b.notify_when_edit(h)


    def soldHouse(self, house):
        self.__company.removeHouseFromListing(house)
        # remove the house from the buyer's watch list
        self.__company.removeHouseFromSaveForLater(house)

    # print all potential buyers who are interested in buying that house
    def printPotentalBuyers(self, house):
        self.__company.getBuyersByHouse(house)        

    def display(self):
        super().display()
        print(f"Position = {self.__position}")
    
    #add notifications to agent
    def notify_when_add(self, house):
        print(f"Dear agent: {super().firstName} {super().lastName}, the following house has been added:")
        house.display()
    #remove notifications to agent
    def notify_when_remove(self, house):
        print(f"Dear agent: {super().firstName} {super().lastName}, the following house has been removed:")
        house.display()
    #edit notifications to agent
    def notify_when_edit(self, house):
        print(f"Dear agent: {super().firstName} {super().lastName}, the following house has updated the price:")
        house.display()


def main():
    owner1 = Owner('Peter', 'Li', '510-111-2222', 'peter@yahoo.com')
    owner2 = Owner('Carl', 'Buck', '408-111-2222', 'carl@yahoo.com')

    house1 = House('1111 Mission Blvd', 1000, 2, 1000000)
    house2 = House('2222 Mission Blvd', 2000, 3, 1500000)
    house3 = House('3333 Mission Blvd', 3000, 4, 2000000)

    owner1.addHouse(house1)
    owner2.addHouse(house2)
    owner2.addHouse(house3)

    buyer1 = Buyer('Tom', 'Buke', '408-555-2222', 'tom@yahoo.com')
    buyer2 = Buyer('Lily', 'Go', '510-222-3333', 'lily@yahoo.com')

    company = Company('Good Future Real Estate')
    agent1 = Agent('Dave', 'Henderson', '408-777-3333',
                   'dave@yahoo.com', 'Senior Agent', company)
    company.addAgent(agent1)

    agent1.addHouseToListingForOwner(owner1, house1) 
    agent1.addHouseToListingForOwner(owner2, house2) 
    agent1.addHouseToListingForOwner(owner2, house3) 

    agent1.helpBuyerToSaveForLater(buyer1, house1) 
    agent1.helpBuyerToSaveForLater(buyer1, house2)
    agent1.helpBuyerToSaveForLater(buyer1, house3)

    agent1.helpBuyerToSaveForLater(buyer2, house2)
    agent1.helpBuyerToSaveForLater(buyer2, house3)

    agent1.editHousePrice('2222 Mission Blvd', 1200000)



    print('\nAfter one house was sold ..........................')
    agent1.soldHouse(house3)



if __name__ == "__main__":
    main()
