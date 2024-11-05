# FUNCTIONS IN PYTHON
# Number 1, 1
def Area_of_Rectangle(width, height):
    # Calculate the area
    return width * height

# Get user input
print("Number 1,1")
width = int(input("Enter Width: "))
height = int(input("Enter Height: "))

# Call the function and print the result
print("Calculating Area...")
print("The area of the rectangle is:", Area_of_Rectangle(width, height))

# Number 1, 2
def addition(x, y, z):
    return x + y + z

def subtraction(x, y, z):
    return x - y - z

def multiplication(x, y, z):
    return x * y * z

def division(x, y, z):
    # To avoid division by zero error
    if y == 0 or z == 0:
        return "Error: Division by zero is not allowed"
    return x / y / z

print("Number 1,2")
x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))
z = int(input("Enter Third Number: "))

def calculator():
    print("What operation would you like to perform?")
    print("NOTE: [Addition = 1, Subtraction = 2, Multiplication = 3, Division = 4]")
    
    # Capture and convert user choice to an integer
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        print("Result:", addition(x, y, z))
    elif choice == 2:
        print("Result:", subtraction(x, y, z))
    elif choice == 3:
        print("Result:", multiplication(x, y, z))
    elif choice == 4:
        print("Result:", division(x, y, z))
    else:
        print("Invalid choice, please try again.")

calculator()

# MODULES
# Number 2,1
import math

# 1. Calculate the square root of a user-provided number
print("Number 2,a")
number = float(input("Enter a number to find its square root: "))
sqrt_result = math.sqrt(number)
print(f"The square root of {number} is: {sqrt_result}")

# 2. Calculate the factorial of a user-provided integer
print("Number 2,b")
number = int(input("Enter a non-negative integer to find its factorial: "))
if number >= 0:
    factorial_result = math.factorial(number)
    print(f"The factorial of {number} is: {factorial_result}")
else:
    print("Factorial is not defined for negative numbers.")

# 3. Calculate the area of a circle using user-provided radius and pi
print("Number 2,c")
radius = float(input("Enter the radius of a circle to calculate its area: "))
area_of_circle = math.pi * (radius ** 2)
print(f"The area of a circle with radius {radius} is: {area_of_circle:.2f}")

# Number 2,2
# main_script.py

import my_module

# Get user input
print("Number 2,2")
number = float(input("Enter a number to find its square: "))

# Use the square function from my_module
result = my_module.square(number)
print(f"The square of {number} is: {result}")

# ERROR EXCEPTION HANDLING
# Number 3,1
def divide_numbers():
    try:
        # Get user input for the numbers
        print("Number 3,1")
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        
        # Perform the division
        result = numerator / denominator
        print(f"The result of the division is: {result}")
    
    except ZeroDivisionError:
        # Handle the division by zero error
        print("Error: Division by zero is not allowed. Please enter a non-zero denominator.")

# Call the function
divide_numbers()

# Number 3,2
def divide_numbers():
    try:
        # Get user input for the numbers
        print("Number 3,2")
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        
        # Perform the division
        result = numerator / denominator
    
    except ZeroDivisionError:
        # Handle division by zero error
        print("Error: Division by zero is not allowed. Please enter a non-zero denominator.")
    
    else:
        # Executes if no exception was raised
        print(f"The result of the division is: {result}")

# Call the function
divide_numbers()

# Number 3,3
class NegativeNumberError(Exception):
    # """Custom exception for negative number input."""
    print("Number 3,3")
    def __init__(self, number):
        super().__init__(f"Invalid input: {number}. The number must be non-negative.")


def check_positive(number):
    if number < 0:
        raise NegativeNumberError(number)
    else:
        print(f"The number {number} is non-negative.")


try:
    num = float(input("Enter a number: "))
    check_positive(num)
except NegativeNumberError as e:
    print(e)

# Number 3,4
def divide_numbers():
    try:
        # Get user input for the numbers
        print("Number 3,4")
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        
        # Perform the division
        result = numerator / denominator
        print(f"The result of the division is: {result}")
    
    except ZeroDivisionError:
        # Handle division by zero error
        print("Error: Division by zero is not allowed.")
    
    finally:
        # This block will always execute
        print("Thank you for using the division calculator.")

# Call the function
divide_numbers()

# WORKING WITH FILE OBJECTS
# Number 4,1
# Open the file in write mode. If the file doesn't exist, it will be created.
print("Number 4,1")
file = open("my_file.txt", "w")

# Write some text into the file
file.write("Hello! This is a new text file.\n")
file.write("Here is some sample text to demonstrate file writing in Python.\n")

# Close the file to ensure changes are saved
file.close()

# # Use 'with' to open the file, which will ensure it gets closed automatically
# with open("my_file.txt", "w") as file:
#     file.write("Hello! This is a new text file.\n")
#     file.write("Here is some sample text to demonstrate file writing in Python.\n")

# # The file is automatically closed after the with block


# NUMBER 4,2
# Specify the filename
print("Number 4,2")
filename = "my_file.txt"  # Make sure this file exists in the same directory

try:
    # Open the file in read mode
    with open(filename, "r") as file:
        # Read the content of the file
        content = file.read()
        
    # Print the content to the console
    print("Contents of the file:")
    print(content)

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")

# Number 4,3
# Specify the filename
print("Number 4,3")
filename = "my_file.txt"  # Make sure this file already exists

# Get user input
user_input = input("Enter the text you want to append to the file: ")

# Open the file in append mode
file = open(filename, "a")  # "a" mode is for appending

# Write the user input to the file
file.write(user_input + "\n")  # Adding a newline for better formatting

# Close the file to ensure changes are saved
file.close()

print("Your input has been appended to the file.")

# Number 5,1
print("Number 5,1")
# Step 1: Ensure Python and pip are Installed
# Check Python Installation: Open your terminal 
# (Command Prompt on Windows, Terminal on macOS/Linux) and run the following command:
# python --version

# Check pip Installation: Verify if pip is installed by running:
#  pip --version

# Step 2: Open Terminal or Command Prompt / Activate the Virtual Environment:
# Run the following command to activate your virtual environment:
# For Windows:
# venv\Scripts\activate
# venv\Scripts\activate
# For macOS/Linux:
# source venv/bin/activate

# Step 3: Install the External Module Using pip
# pip install requests
# if already installed: should print Requirement already satisfied

# Step 4: Verify Installation
# pip show requests


# Number 5,2
print("Number 5,2")
import requests

# Define the URL of the public API
url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    # Make a GET request to the API
    response = requests.get(url)
    
    # Print the response status code
    print(f"Response Status Code: {response.status_code}")
    
    # Print the response data (JSON)
    if response.status_code == 200:
        print("Response Data:")
        print(response.json())  # Parse and print the JSON response
    else:
        print("Failed to retrieve data.")
        
except requests.exceptions.RequestException as e:
    # Print the exception if any error occurs during the request
    print(f"An error occurred: {e}")

# Number 5,3
print("Number 5,3")
import sys
filename = "webscraper.py"  # Make sure this file exists in the same directory

try:
    # Open the file in read mode
    with open(filename, "r") as file:
        # Read the content of the file
        content = file.read()         
    
    # Execute the content of the file
    exec(content)

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    print("Script closed successfully. Thanks for using the program!")
    sys.exit()  # This will terminate the script