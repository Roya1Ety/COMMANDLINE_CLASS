# class Car:

#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def car_type(self):
#         return f"I like {self.make} {self.model} {self.year} car"

# print("input details:")    
# make = input("Enter model:")
# model = input("Enter model:")
# year = input("Enter year:")

# car = Car(model, make, year)
# print(Car.car_type(self))


# car1 = 
# car2 = 


# print(car.make)
# print(car.model)
# print(car.year)
# print(car.car_type())

# class Person:
    
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
    
#     def my_info(self):
#         return f"My name is {self.name}, I'm {self.age} years old, I'm also a {self.gender}

# 3 3 3 3 3  3 3 3 3 3 3 3 3 3  3 (oop with python2)

# class Car:
#     def __init__(self, make, model, year, speed=0):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.speed = speed

#     def accelerate(self, increase):
#         self.speed += increase
#         return f"{self.make} speed increase by {self.speed} km/hr"
    
#     def brake(self, decrease):
#         self.speed -= decrease
#         return f"{self.make} speed decrease by {self.speed} km/hr"
    
#     def __str__(self):
#         return f"I like {self.make} {self.model} {self.year} at {self.speed} km/hr"
    
# car1 = Car("Honda", "Accord", "2017")

# print(car1)
# speed = input("Enter speed to accelerate to:")
# print(car1.accelerate(self.speed))
# # print(car1.accelerate(50))
# print(car1)
# print(car1.brake(20))
# print(car1)
        

# CLASS-WORK CLASS-WORK CLASS-WORK CLASS-WORK CLASS-WORK CLASS-WORK CLASS-WORK CLASS-WORK CLASS-WORK


# WRONG WRONG WRONG 
# class BankAccount:
#     def __init__(self, accountnumber, balance=0):
#         self.accountnumber = accountnumber
#         self.balance = balance
#         print(f"Account successfully created accountnumber is:{self.accountnumber} and accountbalance is: {self.balance}")
#         print(f"would you like to perform any operation: YES= 1, NO = 2")
# choice = 1,2
# if choice == 1:
#     print("Customer Service, what operation would you like to perform: deposit = 1, withdrawal = 2:")
    

#     def deposit(self, depositmethod, amountdeposited):
#         self.depositmethod = depositmethod
#         self.amountdeposited = amountdeposited
#         self.balance += amountdeposited
#         return f"{self.accountnumber} deposited {self.amountdeposited} and new balance is {self.balance}"
    
#     def withdrawal(self, withdrawalmethod, amountwithdrawn):
#         self.withdrawalmethod = withdrawalmethod
#         self.amountwithdrawn = amountwithdrawn
#         self.balance -= amountwithdrawn
#         return f"{self.accountnumber} withdrew {self.amountwithdrawn} and new balance is {self.balance}"
    
    
#     choice1 = 1, 2
#     if choice1 == 1:
#         print(deposit)
    
#     elif choice1 == 2:
#         print(withdrawal)

#     else:
#         print("User Error")


# accountnumber1 = BankAccount("0000000000")

# print(accountnumber1)

# CORRECTION CORRECTION CORRECTION
# class BankAccount:
#     def __init__(self, account_number, balance=0):
#         self.account_number = account_number
#         self.balance = balance
#         print(f"Account successfully created. Account Number: {self.account_number}, Initial Balance: {self.balance}")

#     def deposit(self, amount):
#         self.balance += amount
#         return f"Deposited {amount}. New balance is {self.balance}"

#     def withdraw(self, amount):
#         if amount > self.balance:
#             return "Insufficient funds."
#         self.balance -= amount
#         return f"Withdrew {amount}. New balance is {self.balance}"


# # Create a bank account
# account = BankAccount("0000000000")

# # Ask if the user wants to perform an operation
# while True:
#     choice = input("Would you like to perform any operation? (1 for YES, 2 for NO): ")
#     if choice == '1':
#         operation = input("Choose an operation: 1 for Deposit, 2 for Withdrawal: ")
        
#         if operation == '1':
#             amount = float(input("Enter amount to deposit: "))
#             print(account.deposit(amount))
#             print("Thank you for using our Services")
        
#         elif operation == '2':
#             amount = float(input("Enter amount to withdraw: "))
#             print(account.withdraw(amount))
        
#         else:
#             print("Invalid operation choice.")
#     elif choice == '2':
#         print("Thank you for using our service.")
#         break
#     else:
#         print("Invalid choice. Please enter 1 or 2.")


# RETRY RETRY RETRY RETRY RETRY RETRY RETRY RETRY RETRY
# class BankAccount:
#     def __init__(self, accountnumber, balance=0):
#         self.an = accountnumber
#         self.balance = balance

#     def deposit(self, amount):
#         self.amount = amount
#         self.balance += amount
#         return f"accountnumber:{self.an} deposited {self.amount} new balance:{self.balance}"
    
#     def withdraw(self, amount):
#         self.amount = amount
#         self.balance -= amount
#         return f"accountnumber:{self.an} withdrew {self.amount} new balance:{self.balance}"
    
#     def __str__(self):
#         return f"accountnumber:{self.an} with balance:{self.balance}"
    
# accountnumber = BankAccount("00000")

# print(accountnumber)
# print(accountnumber.deposit(5000))
# print(accountnumber)
# print(accountnumber.withdraw(2000))
# print(accountnumber)

class Phone:
    def __init__(self, brand, model, storage, color):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.color = color

    def make_call(self):
        print(f"Calling from {self.brand} {self.model}...")

# Creating an instance of Phone
my_phone = Phone("Apple", "iPhone 14", "256GB", "Black")

# Calling the make_call method
my_phone.make_call()

