from abc import ABC, abstractmethod

    
class Displayable(ABC):
    @abstractmethod
    def display(self) -> None:
        pass

class Option:
    def __init__(self, enhanced_safety_feature: int, security: int, entertainment: int, sunroof: int) -> None:
        self.__enhanced_safety_feature = enhanced_safety_feature
        self.__security = security
        self.__entertainment = entertainment
        self.__sunroof = sunroof

    @property
    def enhanced_safety_feature(self) -> int:
        return self.__enhanced_safety_feature
    @property
    def security(self) -> int:
        return self.__security    
    @property
    def entertainment(self) -> int:
        return self.__entertainment
    @property
    def sunroof(self) -> int:
        return self.__sunroof       
    

    def display(self) -> None:
        print(self)

    def __str__(self) -> str:
        output = f"enhanced_safety_feature = {self.__enhanced_safety_feature}\nsecurity = {self.__security}\nentertainment = {self.__entertainment}\nsunroof = {self.__sunroof}"
        return output 

    def __repr__(self) -> str:
        return str(self)  


class Vehicle(Displayable):
    def __init__(self, model: str, color: str, model_year: int) -> None:
        self.__model = model
        if isinstance(self, Sedan):
            self.__base_price = 30000
        elif isinstance(self, Truck):
            self.__base_price = 35000
        elif isinstance(self, SUV):
            self.__base_price = 40000
        elif isinstance(self, Minivan):
            self.__base_price = 45000                    
        self.__color = color
        self.__model_year = model_year
        self.__options: list[Option] = []


    @property
    def model(self) -> str:
        return self.__model
    
    @property
    def base_price(self) -> int:
        return self.__base_price

    @property
    def color(self) -> str:
        return self.__color
    
    @property
    def model_year(self) -> int:
        return self.__model_year
    
    @property # only used for evaluation (==)
    def options(self) -> list[Option]:
        return self.__options
    
    def add_option(self, option: Option) -> None:
        self.__options.append(option)

    def calculate_final_price(self) -> int:
        final_price = self.base_price
        for o in self.__options:
            final_price += o.enhanced_safety_feature * 3000
            final_price += o.security * 1000
            final_price += o.entertainment * 2000
            final_price += o.sunroof * 2500

        return final_price    
    
    def display(self) -> None:
        print(self)    
            
    def __str__(self) -> str:
        output = f"model = {self.__model}\nbase_price = {self.__base_price}\ncolor = {self.__color}\nmodel_year = {self.__model_year}\n"        
        for o in self.__options:
            output += f"{o}"
        return output 

    def __repr__(self) -> str:
        return str(self)          


class Sedan(Vehicle):
    def __init__(self, model: str, color: str, model_year: int, transmission: str, package: str) -> None:
        super().__init__(model, color, model_year)
        self.__transmission = transmission
        self.__package = package

    @property
    def transmission(self) -> str:
        return self.__transmission

    @property
    def package(self) -> str:
        return self.__package
        

    def display(self) -> None:
        super().display()
        print(f"transmission = {self.__transmission}\npackage = {self.__package}")




class Truck(Vehicle):
    def __init__(self, model: str, color: str, model_year: int, cargo_bed_size: int, spare_tire_number: int) -> None:
        super().__init__(model, color, model_year)
        self.__cargo_bed_size = cargo_bed_size
        self.__spare_tire_number = spare_tire_number


    @property
    def cargo_bed_size(self) -> int:
        return self.__cargo_bed_size

    @property
    def spare_tire_number(self) -> int:
        return self.__spare_tire_number


    def display(self) -> None:
        super().display()
        print(f"cargo_bed_size = {self.__cargo_bed_size}\nspare_tire_number = {self.__spare_tire_number}")
        

class SUV(Vehicle):
    def __init__(self, model: str, color: str, model_year: int, roof_rack: bool, navigation_system: bool) -> None:
        super().__init__(model, color, model_year)
        self.__roof_rack = roof_rack 
        self.__navigation_system = navigation_system


    @property
    def roof_rack(self) -> bool:
        return self.__roof_rack

    @property
    def navigation_system(self) -> bool:
        return self.__navigation_system

    def display(self) -> None:
        super().display()
        print(f"roof_rack = {self.__roof_rack}\nnavigation_system = {self.__navigation_system}")


class Minivan(Vehicle):
    def __init__(self, model: str, color: str, model_year: int, seat_capacity: int, hybrid_battery_warranty_months: int) -> None:
        super().__init__(model, color, model_year)
        self.__seat_capacity = seat_capacity
        self.__hybrid_battery_warranty_months = hybrid_battery_warranty_months
 

    @property
    def seat_capacity(self) -> int:
        return self.__seat_capacity

    @property
    def hybrid_battery_warranty_months(self) -> int:
        return self.__hybrid_battery_warranty_months

    def display(self) -> None:
        super().display()
        print(f"seat_capacity = {self.__seat_capacity}\nhybrid_battery_warranty_months = {self.__hybrid_battery_warranty_months}")


class Dealer(Displayable):
    def __init__(self, name: str, address: str) -> None:
        self.__name = name
        self.__address = address
        self.__vehicles: list[Vehicle] = []
    
    @property
    def name(self) -> str:
        return self.__name

    @property    
    def address(self) -> str:
        return self.__address
 

    def add_vehicle(self, vehicle: Vehicle) -> None:
        self.__vehicles.append(vehicle)


    def remove_vehicle(self, vehicle: Vehicle) -> None:
        # for v in self.__vehicles:
            # if v == vehicle:
                # self.__vehicles.remove(vehicle)
        
        for v in self.__vehicles:
            if v.model == vehicle.model and v.color == vehicle.color and v.model_year == vehicle.model_year:
                for o in v.options:
                    for o_ in vehicle.options:
                        if o.enhanced_safety_feature == o_.enhanced_safety_feature and o.security == o_.security and o.entertainment == o_.entertainment and o.sunroof == o_.sunroof:
                            self.__vehicles.remove(v)


    def __iter__(self):
        self.__index = -1
        return self

    def __next__(self):
        if self.__index >= len(self.__vehicles) - 1:
            raise StopIteration()
        self.__index += 1
        vehicle = self.__vehicles[self.__index]
        return vehicle
    

    def display(self) -> None:
        print(f"dealer_name = {self.__name}\naddress = {self.__address}")
        print(f"The dealership has the following vehicles: ")
        for v in self.__vehicles:
            v.display()
            print()


    def show_available(self) -> None:
        for v in self.__vehicles:
            v.display()
            print()


    def search_and_display(self, type = '', model = '', color = '', model_year = 0,\
                            roof_rack = False, navigation_system = False, transmission = '', package = '',\
                                  cargo_bed_size = 0, spare_tire_number = 0, seat_capacity = 0, hybrid_battery_warranty_months = 0) -> None:
        display_list: list[Vehicle] = []
        if type == 'SUV':
            for v in self.__vehicles:
                if isinstance(v, SUV):
                    display_list.append(v)
                    
        elif type == 'Sedan':
            for v in self.__vehicles:
                if isinstance(v, Sedan):
                    display_list.append(v)

        elif type == 'Truck':
            for v in self.__vehicles:
                if isinstance(v, Truck):
                    display_list.append(v)

        elif type == 'Minivan':
            for v in self.__vehicles:
                if isinstance(v, Minivan):
                    display_list.append(v)

        for v in self.__vehicles:
            if v.model == model:
                display_list.append(v)
            if v.color == color:
                display_list.append(v)
            if v.model_year == model_year:
                display_list.append(v)

        for v in self.__vehicles:
            if isinstance(v, SUV):
                if v.roof_rack == roof_rack:
                    display_list.append(v)
                if v.navigation_system == navigation_system:
                    display_list.append(v)
            
            if isinstance(v, Sedan):
                if v.transmission == transmission:
                    display_list.append(v)
                if v.package == package:
                    display_list.append(v)

            if isinstance(v, Truck):
                if v.cargo_bed_size == cargo_bed_size:
                    display_list.append(v)
                if v.spare_tire_number == spare_tire_number:
                    display_list.append(v)

            if isinstance(v, Minivan):
                if v.seat_capacity == seat_capacity:
                    display_list.append(v)
                if v.hybrid_battery_warranty_months == hybrid_battery_warranty_months:
                    display_list.append(v)

        for v in display_list:
            v.display()
      
class User:
    def __init__(self, name: str) -> None:
        self.__name = name

    def name(self) -> str:
        return self.__name
      
    def find_least_expensive(self, dealer: Dealer) -> Vehicle:
        least_expensive = 99999999999
        for v in dealer:
            final_price = v.calculate_final_price()
            if final_price < least_expensive:
                least_expensive = final_price
                return v

    def find_most_expensive(self, dealer: Dealer) -> Vehicle:
        most_expensive = 0
        for v in dealer:
            final_price = v.calculate_final_price()
            if final_price > most_expensive:
                most_expensive = final_price
                return v


    def price_calculation(self, type: str, model: str, color: str, model_year: int,\
                           enhanced_safety_feature: int, security: int, entertainment: int, sunroof: int,\
                            roof_rack = False, navigation_system = False, transmission = 'Manual', package = 'Basic Package',\
                                  cargo_bed_size = 0, spare_tire_number = 0, seat_capacity = 0, hybrid_battery_warranty_months = 0) -> int:
        if type == 'SUV':
            new_vehicle = SUV(model, color, model_year, roof_rack, navigation_system)
            new_vehicle.add_option(Option(enhanced_safety_feature, security, entertainment, sunroof))
            final_price = new_vehicle.calculate_final_price()
            return final_price

        elif type == 'Sedan':
            new_vehicle = Sedan(model, color, model_year, transmission, package)
            new_vehicle.add_option(Option(enhanced_safety_feature, security, entertainment, sunroof))
            final_price = new_vehicle.calculate_final_price()
            return final_price

        elif type == 'Truck':
            new_vehicle = Truck(model, color, model_year, cargo_bed_size, spare_tire_number)
            new_vehicle.add_option(Option(enhanced_safety_feature, security, entertainment, sunroof))
            final_price = new_vehicle.calculate_final_price()
            return final_price

        elif type == 'Minivan':
            new_vehicle = Minivan(model, color, model_year, seat_capacity, hybrid_battery_warranty_months)
            new_vehicle.add_option(Option(enhanced_safety_feature, security, entertainment, sunroof))
            final_price = new_vehicle.calculate_final_price()
            return final_price


def main():
    print('--------------------------------')
    print('Define SUV: ')
    suv1 = SUV('Rav4','red', 2021, True, True)
    suv1.add_option(Option(1, 1, 1, 1))
    suv1.display()
    suv_final_price = suv1.calculate_final_price()
    print("The final price of SUV is", suv_final_price)
    print('--------------------------------')
    print()
    
    print('--------------------------------')
    print('Define Sedan: ')
    sedan1 = Sedan('Camry', 'blue', 2022, 'Automatic', 'Sports Package')
    sedan1.add_option(Option(1, 2, 1, 1))
    sedan1.display()
    sedan_final_price = sedan1.calculate_final_price()
    print("The final price of sedan is", sedan_final_price)
    print('--------------------------------')
    print()
    
    print('--------------------------------')
    print('Define Truck: ')
    truck1 = Truck('Tacoma', 'white', 2023, 20, 2)
    truck1.add_option(Option(2, 3, 2, 1))
    truck1.display()
    truck_final_price = truck1.calculate_final_price()
    print("The final price of truck is", truck_final_price)
    print('--------------------------------')
    print()
    
    print('--------------------------------')
    print('Define Minivan: ')
    mini1 = Minivan('Wayne', 'black', 2020, 7, 12)
    mini1.add_option(Option(1, 0, 0, 0))
    mini1.display()
    mini_final_price = mini1.calculate_final_price()
    print("The final price of minivan is", mini_final_price)
    print('--------------------------------')
    print()    
    
    print('--------------------------------')
    print('Define Dealership: ')
    dealer = Dealer("XYZ Car Dealership", "I-4 Million Mall")
    dealer.add_vehicle(suv1)
    dealer.add_vehicle(truck1)
    dealer.add_vehicle(mini1)
    dealer.add_vehicle(sedan1)
    dealer.display()
    print('--------------------------------')
    print()
    
    print('--------------------------------')
    print('The removal vehicle is:')
    vehicle_removal = Minivan('Wayne', 'black', 2020, 7, 12)
    vehicle_removal.add_option(Option(1, 0, 0, 0))
    vehicle_removal.display()
    print()


    print('Dealership after removing vehicle:')
    dealer.remove_vehicle(vehicle_removal)
    dealer.display()
    print('--------------------------------')
    print()


    print('Show available vehicles at the dealership:')
    dealer.show_available()
    print('--------------------------------')
    print()

    print('--------------------------------')
    print('Search and Display: ')
    dealer.search_and_display(model = 'Camry')
    print()

    dealer.search_and_display(color = 'white')
    print()

    dealer.search_and_display(type = 'Sedan')
    print()

    dealer.search_and_display(model_year = 2023)
    print()

    dealer.search_and_display(navigation_system = True)
    print()

    dealer.search_and_display(transmission = 'Automatic')
    print()

    dealer.search_and_display(cargo_bed_size=20)
    print()

    dealer.search_and_display(spare_tire_number=2)
    print()

    dealer.search_and_display(roof_rack = True)
    print()

    dealer.search_and_display(navigation_system=True)
    print()

    dealer.search_and_display(seat_capacity=7)
    print()

    dealer.search_and_display(hybrid_battery_warranty_months=12)
    print()

    print('--------------------------------')
    print()
 
    print('--------------------------------')
    user = User('Allison Ding')
    print(f"The least expensive vehicle is:")
    least_expensive = user.find_least_expensive(dealer)
    least_expensive.display()
    print('--------------------------------')
    print()
 
    print('--------------------------------')
    print(f"The most expensive vehicle is:")
    most_expensive = user.find_most_expensive(dealer)
    most_expensive.display()
    print('--------------------------------')
    print()

    print('--------------------------------')
    print("Create the vehicles of your wishes with the desired options and calculate the final price:")
    type = 'SUV'
    model = 'Yosemite'
    color = 'grey'
    model_year = 2024
    enhanced_safety_feature = 1
    security = 1
    entertainment = 1
    sunroof = 1
    roof_rack = 3
    navigation_system = True
    price = user.price_calculation(type = type, model = model, color = color, model_year = model_year, enhanced_safety_feature = enhanced_safety_feature, security = security, entertainment = entertainment, sunroof = sunroof, roof_rack = roof_rack, navigation_system = navigation_system)
    print(type, model, 'in', color, 'of model year of', model_year, 'with', enhanced_safety_feature, 'enhanced safety feature and', security, 'security and', entertainment, 'entertainment and', sunroof, 'sunroof is', price)

    type1 = 'Sedan'
    model1 = 'Yosemite'
    color1 = 'blue'
    model_year1 = 2020
    enhanced_safety_feature1 = 2
    security1 = 2
    entertainment1 = 2
    sunroof1 = 2
    transmission1 = 'Automatic'
    package1 = 'Sports Package'
    price = user.price_calculation(type = type1, model = model1, color = color1, model_year = model_year1, enhanced_safety_feature = enhanced_safety_feature1, security = security1, entertainment = entertainment1, sunroof = sunroof1, transmission = transmission1, package = package1)
    print(type1, model1, 'in', color1, 'of model year of', model_year1, 'with', enhanced_safety_feature1, 'enhanced safety feature and', security1, 'security and', entertainment1, 'entertainment and', sunroof1, 'sunroof is', price)
    print('--------------------------------')

    
if __name__ == '__main__':
    main()    