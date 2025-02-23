class Person: # define class Person
    def __init__(self, name: str) -> None:
        self.__name = name

    def dowork(self) -> None:
        print(f"Person {self.__name} is doing nothing.")

    def __str__(self) -> str:
        return f"name = {self.__name}"

    def display(self) -> None:
        print(self)
    
    @property
    def name(self) -> str:
        return self.__name


class Programmer(Person): # define class Programmer with Person as its super class
    def __init__(self, name: str, skills: str, salary: float) -> None:
        super().__init__(name)
        self.__skills = skills # create programmer's own attribute skills 
        self.__salary = salary # create programmer's own attribute salary

    def get_annual_income(self) -> float:
        return self.__salary * 12

    def dowork(self) -> None: # name is inherited from Person class
        print(f"Programmer {super().name} is writing a program.")

    def __str__(self) -> str: # full print is inherited from Person class 
        return f"{super().__str__()}\nskills = {self.__skills}\nsalary = {self.__salary}"

class Manager(Programmer): # define class Manager with Programmer as its super class
    def __init__(self, name: str, skills: str, salary: float, bonus: float) -> None:
       super().__init__(name, skills, salary)
       self.__bonus = bonus # create manager of programmer's own attribute bonus

    def get_annual_income(self) -> float: # create function to calculate annual income
        return super().get_annual_income() + self.__bonus
    
    def dowork(self) -> None: # name is inherited from Programmer class and thus Person class
        print(f"Programmer {super().name} is supervising a team of programmers.")

    def __str__(self) -> str: # full print is inherited from Programmer class. Add bonus to the print as well.
        return f"{super().__str__()}\nbonus = {self.__bonus}"

class Group: # define Group class
    def __init__(self, groupname: str) -> None:
        self.__groupname = groupname 
        self.__members: list[Programmer] = []

    def groupname(self):
        return self.__groupname

    def add_member(self, member:Programmer) -> None:
        self.__members.append(member)
    
    def remove_member(self, name: str):
        for member in self.__members:
            if member.name == name:
                self.__members.pop()

    def ask_anyone_dowork(self):
        for member in self.__members:
            member.dowork() #since member is a programmer, it has dowork method 

    def ask_manager_dowork(self) -> None:
        for member in self.__members:
            if isinstance(member, Manager):
                member.dowork()

    def get_allmembers_morethan(self, income: float) -> list[Programmer]:
        members_morethan: list[Programmer] = []
        for member in self.__members:
            if member.get_annual_income() > income:
                members_morethan.append(member)
        
        return members_morethan

    def __str__(self) -> str:
        # output = f"Groupname: {self.__groupname}\n"
        output = "The group has these members: \n"
        for member in self.__members:
            output += str(member) + "\n\n"
        return output
    
    def display(self):
        print(self)
    
    def __repr__(self) -> str:
        return str(self)

class Project: #define Project class
    def __init__(self, projname: str, budget = 0.0, active = False):
        self.__projname = projname
        self.__budget = budget
        self.__active = active
    
    @property
    def projname(self) -> str:
        return self.__projname
    
    @property
    def budget(self) -> float:
        return self.__budget
    
    @property
    def active(self) -> bool:
        return self.__active
    
    def display(self) -> None:
        print(self)

    def __str__(self) -> str:
        return f"projname = {self.__projname}\nbudget = {self.__budget}\nactive = {self.__active}"


class ITGroup(Group): # define ITGROUP class with Group as superclass.
    def __init__(self, groupname: str) -> None:
        super().__init__(groupname) 
        self.__projects: list[Project] = [] # create own attribute, projects

    def add_project(self, project: Project):
        self.__projects.append(project)
    
    def find_largest_project(self) -> Project:
        largest = 0
        for project in self.__projects: # calculate the largest budget
            largest = max(largest, project.budget)
        
        for project in self.__projects: # identify the project that has the largest budget
            if project.budget == largest:
                return project

    def display(self):
        print(self)


    def get_active_projects(self) -> list[Project]:
        active_projects: list[Project] = []
        for project in self.__projects:
            if project.active == True:
                active_projects.append(project)
        
        return active_projects

    def __str__(self): # return both member information and project information
        output = super().__str__()
        output += "\nThe group has these projects: \n"
        for project in self.__projects:
            output += str(project) + "\n\n"
        return output

def main() -> None:
    p1: Programmer = Programmer("Lily", "C++, Java", 10000)
    p2: Programmer = Programmer("Judy", "Python, Java", 18000)
    m: Manager = Manager("Peter", "Management", 20000, 20000)
    proj1: Project = Project("MAX-5", 200000, True)
    proj2: Project = Project("FOX-4", 100000, False)
    proj3: Project = Project("FOX-XP", 500000, True)

    itgrp: ITGroup = ITGroup("ATX Group")
    itgrp.add_member(p1)
    itgrp.add_member(p2)
    itgrp.add_member(m)
    itgrp.add_project(proj1)
    itgrp.add_project(proj2)
    itgrp.add_project(proj3)
    itgrp.display()

    p3: Programmer = Programmer("Jone", "Python, Java", 1118000)
    itgrp.add_member(p3)

    itgrp.ask_anyone_dowork()
    print()
    itgrp.ask_manager_dowork()
    
    print("\nGet the largest project...")
    maxProj: Optional[Project] = itgrp.find_largest_project()
    if maxProj is not None:
        maxProj.display()
    
    print("\nGet the acive projects...")
    projects: list[Project] = itgrp.get_active_projects()
    for proj in projects:
        proj.display()
        print()

    itgrp.display()
    itgrp.remove_member(p3.name)
    
    print("\nGet the members with high income...")
    members: list[Programmer] = itgrp.get_allmembers_morethan(200000)
    for member in members:
        member.display()
        print()


if __name__ == "__main__":
    main()
