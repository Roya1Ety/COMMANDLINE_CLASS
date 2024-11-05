# ERROR HANDLING
# 1 try:
#     print(100 / 2)
# except Exception as e:
#         print('An error occured:', e)

# 2
# age = input("Enter your age:") 
# age = int(age)
# try:
#     if age >= 18:
#         print(f"You are {age} years old")
# except Exception as e:
#     print('An error occured', e)
# else:
#     print("Invalid number")

# 3
# for else and finally
# num = input("Enter number: ")
# num = int(num)
# try:
#     print(f"100 divided by {num} is {100 / num}")
# except Exception as e:
#     print("An error occured:", e)
# else:
#     print("The number is good")
# finally:
#     print("This will always execute at the end (usually used for file closing and database connectivity, prevents data leaking)")

# def check_age(age):
#     if age < 18:
#         raise ValueError("Your are a minor")
#     return "Advance"

# try:
#     print(check_age(19))
# except ValueError as e:
#     print(e)

# CREATING AN ERROR (PERSONAL ERROR)
class InvalidNumber(Exception):
    def __init__(self, age):
        self.age = age
        super().__init__(f"Invalid age: {self.age}, Age must be a positive number")

def check_age(age):
    if age < 18:
        raise InvalidNumber(age)
    print(f'you are {age} years old')

try:
    check_age(5)
except InvalidNumber as e:
    print(e)

# # working with file object
# content = open("PHYTON\python-ass-wee1.txt", 'r')

# file = content.read()
# print(file)
# content.close()

# with open("PHYTON\python-ass-wee1.txt", 'r') as file:
#     data = file.read()
#     print(data)