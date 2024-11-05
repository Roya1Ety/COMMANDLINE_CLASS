# from abc import ABC

# class car(ABC):
#     pass
#     # def Toyota(self):
#     #     return "This is a Toyota car"
    
#     # def Honda(self):
#     #     return "This is a Honda Car"

# class Toyota(car):
#     def Toyota(self):
#         return "This is a Toyota car"
    
# class Honda(car):
#     def Honda(self):
#         return "This is a Honda car"
    
# car1 = Toyota()
# car2 = Honda()
# print(car1.Toyota())
# print(car2.Honda())

# ENCAPSULATION
# class BankAccount:
#     def __init__(self, deposit):
#         self._balance = deposit  # Initialize balance with the deposit amount

#     def deposit_amount(self, amount):
#         self._balance += amount  # Add amount to the balance
#         return f"You deposited {amount}, your new balance is {self._balance}"

#     def get_balance(self):
#         return f"Your balance is {self._balance}"

# # Create a BankAccount instance with an initial deposit
# bank_account = BankAccount(1000)

# # Example usage
# print(bank_account.get_balance())  # Check initial balance
# print(bank_account.deposit_amount(1000))  # Deposit additional amount
# print(bank_account.get_balance())  # Check updated balance


# REDO REDO REDO REDO REDO REDO REDO REDO REDO REDO REDO
# class BankAccount:
#     def __init__(self, deposit, balance):
#         self._balance = balance + deposit
#         self.deposit = deposit

#     def deposit_amount(self, amount):
#         self.deposit += amount
#         return f"You deposited {amount}, your balance is {self._balance}"
    
#     def get_balance(self):
#         return f"Your balance is {self._balance}"
    
# bank_account = BankAccount(1000)

# print(bank_account.deposit_amount(500))
# print(bank_account.get_balance())

# INHERITANCE
# class Animal:
#     def sound(self):
#         return f"Sound of animal"
    
# class Cat(Animal):
#     def sound(self):
#         return "Meow"
    
# class Dog(Animal):
#     def sound(self):
#         return "Bark"


# def animal_sound(animal):
#     print(animal.sound())
 
# cat = Cat()
# dog = Dog()

# # print(cat.sound())
# # print(dog.sound())

# animal_sound(cat)
# animal_sound(dog)

# OOP WITH PYTHON1 OOP WITH PYTHON1 OOP WITH PYTHON1 OOP WITH PYTHON1 OOP WITH PYTHON1
