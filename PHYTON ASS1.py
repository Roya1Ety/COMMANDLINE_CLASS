# 1. Number data types
# - INT.

# Declare an integer variable
number = 10

# Addition
addition = number + 5
print(addition)

# Subtraction
subtraction = number - 3
print(subtraction)

# Multiplication
multiplication = number * 4
print(multiplication)

# Division
division = number / 2
print(division)


# -FLOAT
# Declare a floating-point variable
number = 10.75

# Addition
addition = number + 5.25
print(addition,{round(addition, 2)})

# Subtraction
subtraction = number - 3.45
print(subtraction,{round(subtraction, 2)})

# Multiplication
multiplication = number * 2.5
print(multiplication,{round(multiplication, 2)})

# Division
division = number / 3.3
print(division,{round(division, 2)})


# -COMPLEX
# Declare two complex numbers
complex_number1 = 4 + 4j
complex_number2 = 6 + 2j

# Add the complex numbers
result = complex_number1 + complex_number2

# Print the real and imaginary parts of the result
print(result.real)
print(result.imag)
# If you want to display the imaginary part with the j symbol, you can manually format it like this:
# python
# Copy code
# # Declare two complex numbers
# complex_number1 = 3 + 4j
# complex_number2 = 1 + 2j
# # Add the complex numbers
# result = complex_number1 + complex_number2
# # Print the real and imaginary parts of the result with 'j' for the imaginary part
# print("Real part:", result.real)
# print("Imaginary part:", str(result.imag) + 'j')


# 2.Text Data
# - STRING
# Take a string input from the user
String_1 = "JESUS"

#Concatenate it with another string
String_2 = "my Savior"
concatenated_string= String_1 + " " + String_2
print(concatenated_string)

#Access a specific character using indexing
indexing = 1, 2, 3, 4, "apple", "banana", 5
print(indexing[4])

#Slice a portion of the string
slicing = concatenated_string
print(slicing[2:7])

#Convert the string to uppercase and lowercase
# print(String_1.lower())
# print(String_2.upper())
# print(String_1.capitalize())


# 3. Boolean Data
# a

# b
statement1 = ("num1")
statement2 = ("num2")
print("Enter Statements")
input("num1")
input("num2")

num1 = int(num1)
num2 = int(num2)

if num1 > num2
    print("greater")
else 
    print("lesser than")


