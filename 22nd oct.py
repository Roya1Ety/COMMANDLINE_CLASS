# # Function
# def greet(name, age):
#     print(f"My name is {name}, I'm {age} years old")

# greet("Alice", 25)


# # import main
# # from main import greet


# SIMPLE CALCULATOR
# def add(x, y):
#     return x+y

# def subtract(x, y):
#     return x-y

# def multiply(x, y):
#     return x*y

# def division(x, y):
#     if x == 0:
#         return "Error division by 0"
#     else:
#         return x/y

# def calculator():
#     print("Enter number")
#     choice = input("Enter your number of choice")
#     num1 = input("Enter First number:")
#     num2 = input("Enter Second number:")

#     num_digit1 = int(num1)
#     num_digit2 = int(num2)

#     if choice == "1":
#         print(add(num_digit1, num_digit2))
#     elif choice == "2":
#         print(subtract(num_digit1, num_digit2))
#     elif choice == "3":
#         print(multiply(num_digit1, num_digit2))
#     elif choice == "4":
#         print(division(num_digit1, num_digit2))
#     else:
#         print("Invalid number of choice")

# calculator()

# phyton module
import math
import random

print(math.sqrt(25))
print(math.pi)

lst_rand = ["orange", "mango", "banana"]
# can be used in generating tokens
print(random.randint(0000000, 9999999))
print(random.choice(lst_rand))
random.shuffle(lst_rand)
print(lst_rand)