# # greet='Hello World'
# # print(greet)

# num =  2 + 4j
# print(type(num))
# # complex number

# # string u either use single or double quote
# # variables must be unique
# text = "My name is" + " " + "Obaloluwa "
# print(text.title() * 5)

# true = True
# false = False

# print(type(true))
# print(type(false))

# print(2 > 7)
# print(2 == 3)
# print(2 == 2)

# tuple(1,)
# print(tuple)

# lst = [1, 2, 3, 4, 2, "apple", "banana", 20.50, 2 + 3j]

# lst.append("mango")
# lst.pop(1)
# # lst.remove(2)
# dex = lst.index(4)
# # print(dex)
# prin(t(lst)

# tup = (1, "apple", "banana", 4, 3, 6, 2+6j)
# tup2= ("mango",)
# # print(type(tup2))
# # print(type(tup))
# # print(tup[2])
# # print(tup.index("apple"))
# tup
# lst = list(tup)
# print(lst.pop(3))
# print(lst)
# print(type(lst))
# print(type(tup))

# unique_number = {"watermelon","banana",  "mango", "orange"}
# unique_number.pop()
# print(type(unique_number))
# print(unique_number)

# name = "OBA"
# age = 20
# city = "New York"
# person = {
#     "name": name,
#     "age": age,
#     "city": city,
# }
# print(type(person))
# print(person.values())
# print(person.items())
# # print(dict)

# name = None
# print(type(name))

x = 10
y = 3

# print(x+y)
# print(x*y)
# print(x-y)
# print(y-x)
# print(x/y)
# print(x ** y)
# print(x % y)
# print(x // y)

# print(x == y)
# print(x >= y)
# print(x <= y)
# print(x > y)
# print(x < y)
# print(x != y)

# name = "Alice"
# person = name

# if name and person == "Alice":
#     print(True)
# else:
#     print(False)

# tup = (1, "apple", "banana", 4, 3, 6, 2+6j)

# if "apples" not in tup:
#     print(True)
# else:
#     print(False)

# x=10
# y=3
 
# print("Yes")  if x > y else print(False)

# x = 10

# x += y
# x -= y
# x *= y
# x **= y
# x /= y

# x %= y

# print(x)

# WORKING WITH VARIABLE
# NAME = "Alice"
# FIRST_NAME = "John"
# # 1name = "book" this is wrong
# # $name = "Alice" also wrong
# _name = "Alice"
# _ = "Alice"

# first_name =  "Alice"
# age = 20
# num = 3.40

# print(_name)

# import keyword

# print(keyword.kwlist)
# is = "light" this is wrong also

# working with strings

# text = "Hello, World"
# number = 1, 2, 3, 4, 5, 6, 7, 8, 9, 0

# print(text[4])
# print(number[4])

# text = "Hello World"
# # print(text[4:6])
# # print(text.replace("World", "phyton"))
# print(text.strip(""))

# text = "Hello"
# text2 = "World"
# conct = text + " " + text2
# print(conct)

# string manipulation

# name = "Alice"
# age = 24

# text = "My name is {} and I am {} years Old". format(name, age)
# print(text)

# text = "My name is {0} and I am {1} years old".format(name, age)

# text = "My name is {name} and I am {age} years old".format(name = "Alice", age = 25)

# print(len(text))


# 16th october 2024
# control structure (number 11)
# age = input("ENTER YOUR AGE:")
# age = int(age)
# has_id = input("Do you have a voter's card (yes/no)?:").lower()

# if age >= 18:
#     print("you are eligible to vote")
#     if has_id == "yes":
#         print("you can go and vote")
#     else:
#         print("but you can't vote without voter's card, get voter's card @obaloluwa.com")
# elif age >=13 <= 17:
#     print("You are a teenager, wait a little more to vote")
#     if has_id == "yes":
#         print("wow, whose management gave you voter's card to vote, before reaching 18yrs")
# else:
#     print("You are a child, stop playing around with phone")

# control structure 2 (number 12)

# a part
# num = 0
# while num <= 10:
#     num += 1
#     if num == 5:
#         break
#     print("Addition of number", num)

# b part
# number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# for num in number:
#     num += 1
#     if num ==1:
#         continue
#     print("Addition of number", num)

# persons = {"Alice": 30, "Bola": 40, "James": 50, "Bolu": 70}

# for name, score in persons.items():
#     print(f"{name} scored {score}")

# text = "I love Jesus"
# for i in range(100):
#     print("I LOVE JESUS")

# text = "I love Jesus"

# for i in range(100):
#     print(text)

# object mapping (no 13)
student = {
    "name": "Alice",
    "age": 24,
    "course": "computer science",
    # "subject": "English"
}

# # create
# student["subject"]= "Mathematics"

# # Retrieve
# retrieve = student["age"]

# # update
# student["course"] = "Marketing"

# # delete 

# del student ["name"]
# student.pop(course)

# print("student data:", student)
# print("Retrieve  age: ",retrieve)

# student = {
#     "name": "Alice",
#     "age": 24,
#     "course": "computer-science",
#     "subject": "English"
# }

# student.
# for key, value in student.items():
#     print(f"what is your {key}? my {key} is {value}")
#     print(f"what is your {key}? I'm {value} years old")
#     print(f"what is your {key}? I'm doing {value} in school")
#     print(f"what {key} are you doing? I'm doing {value} language")

squared_dict = {x: x**2 for x in range (1, 6)}
print(squared_dict)

# print(list(range))