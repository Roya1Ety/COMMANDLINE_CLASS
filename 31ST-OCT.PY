
# REGEX
# import re
# # import string

# text = "The rain in spain stays mainly in the plain."

# find_all = re.findall(r"in", text)

# search = re.search(r"plain", text)

# sub =re.sub(r"Spain", "France",text )

# split= re.split(r" ", text)

# print(find_all)
# # how to print number of times it appears
# print(search)
# print(sub)
# print(split)

# JSON (data manipulation)
import json

person = {
    "name": "Alice",
    "age": 30,
    "email": "royale@gmail.com",
    "verified": False
}

print(person)

json_dumps = json.dumps(person)

print(json_dumps)

phyton_load = json.loads(json_dumps)

print(phyton_load)

with open("json_text.json" "w") as json_file:
    # json_file = 
    json.dump(person, json_file)
    # print(json_file)

with open("json_text.json", "r") as json_file:
    py_file = json.load(json_file)
    print("file convert to PY object:",py_file)