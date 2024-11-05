
# 1. Creating a class
class Phone:
    def __init__(self, brand, model, storage, color):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.color = color

    def make_call(self):
        print(f"Calling from {self.brand} {self.model} {self.storage} {self.color}")

my_phone = Phone("Apple", "iPhone 14", "256GB", "Black", "house")

my_phone.make_call()

class Phone:
    def __init__(self, brand, model, storage, color):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.color = color

    def make_call(self, number):
        return f"Calling {number} from {self.brand} {self.model}..."
    
my_phone = Phone("Apple", "iPhone 13", "256GB", "black")

print("Brand:", my_phone.brand)
print("Model:", my_phone.model)
print("Storage:", my_phone.storage)
print("Color:", my_phone.color)

# Calling the make_call method
print(my_phone.make_call("07046369645"))


# 2. Modeling Real-World Objects with OOP

# A. Create a Class for a Real-World Object
class Car:
    def __init__(self, make, model, year):
        self.make = make       
        self.model = model     
        self.year = year       
        self.odometer = 0      
    def drive(self, miles):
        """Simulate driving the car a certain number of miles."""
        if miles < 0:
            print("Miles driven cannot be negative.")
        else:
            self.odometer += miles
            print(f"You drove {miles} miles. Total mileage: {self.odometer} miles.")

    def display_info(self):
        """Display information about the car."""
        return f"{self.year} {self.make} {self.model} with {self.odometer} miles."


my_car = Car("Toyota", "Camry", 2022)

my_car.drive(150)
print(my_car.display_info())

# B. Demonstrate Encapsulation
class Car:
    def __init__(self, make, model, year):
        self.__year = year          
        self.__make = make          
        self.__model = model       
        self.__odometer = 0         

    
    def get_make(self):
        return self.__make

    
    def set_make(self, make):
        self.__make = make

    
    def get_model(self):
        return self.__model

    
    def set_model(self, model):
        self.__model = model

    
    def get_year(self):
        return self.__year

    
    def set_year(self, year):
        if year > 1885:  
            self.__year = year
        else:
            print("Invalid year. Cars were not produced before 1886.")

    
    def get_odometer(self):
        return self.__odometer

    
    def drive(self, miles):
        """Simulate driving the car a certain number of miles."""
        if miles < 0:
            print("Miles driven cannot be negative.")
        else:
            self.__odometer += miles
            print(f"You drove {miles} miles. Total mileage: {self.__odometer} miles.")

    
    def display_info(self):
        """Display information about the car."""
        return f"{self.__year} {self.__make} {self.__model} with {self.__odometer} miles."


my_car = Car("Toyota", "Camry", 2022)


print(my_car.display_info())
my_car.drive(150)
print(my_car.get_odometer())

my_car.set_make("Honda")
print(my_car.get_make())

my_car.set_model("Accord")
print(my_car.get_model())

# Set an invalid year
my_car.set_year(1800)  # Should print an error message

# C. Demonstrate Inheritance
class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__odometer = 0

    
    def get_make(self):
        return self.__make

    
    def set_make(self, make):
        self.__make = make

    
    def get_model(self):
        return self.__model

    
    def set_model(self, model):
        self.__model = model

    
    def get_year(self):
        return self.__year

    
    def set_year(self, year):
        if year > 1885:
            self.__year = year
        else:
            print("Invalid year. Cars were not produced before 1886.")

    
    def get_odometer(self):
        return self.__odometer

    
    def drive(self, miles):
        """Simulate driving the car a certain number of miles."""
        if miles < 0:
            print("Miles driven cannot be negative.")
        else:
            self.__odometer += miles
            print(f"You drove {miles} miles. Total mileage: {self.__odometer} miles.")

    
    def display_info(self):
        """Display information about the car."""
        return f"{self.__year} {self.__make} {self.__model} with {self.__odometer} miles."


class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size=75):
        super().__init__(make, model, year)  
        self.__battery_size = battery_size   

    
    def get_battery_size(self):
        return self.__battery_size

    
    def charge(self):
        """Simulate charging the electric car."""
        print(f"The {self.get_make()} {self.get_model()} is now fully charged.")

    
    def display_info(self):
        """Display information specific to an electric car."""
        car_info = super().display_info()  
        return f"{car_info} with a {self.__battery_size}-kWh battery."


my_electric_car = ElectricCar("Tesla", "Model S", 2022, battery_size=100)


print(my_electric_car.display_info())
my_electric_car.drive(200)
my_electric_car.charge()

# D. Demonstrate Polymorphism
class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__odometer = 0

    # Method to display car information
    def display_info(self):
        """Display general information about the car."""
        return f"{self.__year} {self.__make} {self.__model} with {self.__odometer} miles."

    # Method to drive and update odometer
    def drive(self, miles):
        """Simulate driving the car a certain number of miles."""
        if miles < 0:
            print("Miles driven cannot be negative.")
        else:
            self.__odometer += miles
            print(f"You drove {miles} miles. Total mileage: {self.__odometer} miles.")

# Subclass ElectricCar inherits from Car
class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size=75):
        super().__init__(make, model, year)
        self.__battery_size = battery_size

    # Overriding the display_info method to show additional info specific to ElectricCar
    def display_info(self):
        """Display detailed information specific to an electric car."""
        return f"Electric {super().display_info()} with a {self.__battery_size}-kWh battery."

    # Additional method specific to ElectricCar
    def charge(self):
        """Simulate charging the electric car."""
        print(f"The {self.get_make()} {self.get_model()} is now fully charged.")

# Polymorphism demonstration
def show_car_info(car):
    print(car.display_info())

# Instantiate Car and ElectricCar
gas_car = Car("Ford", "Mustang", 2021)
electric_car = ElectricCar("Tesla", "Model S", 2022, battery_size=100)

# Using the same function to display information for both types of cars
show_car_info(gas_car)        # Calls Car's display_info method
show_car_info(electric_car)   # Calls ElectricCar's overridden display_info method
