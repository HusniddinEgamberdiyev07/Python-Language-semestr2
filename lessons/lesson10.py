# JSON ( javascript object notation )

# It is in string format

# Client <- Internet -> Server -> DataBase
#        JSON        JSON       table

# Json is light weight. Humans can read it easily. Easy to parse.
# Compiler or interpreter has parser.

# Json helps to:

# Data exchange between systems.
# Configuration files.
# DataStorage -> no sql database like mongodb stores data in json
# Web development -> local storage, ajax requests, SOAP, REST

import json

# json.dumps() -> py to json
# json.loads() -> json to py

print("\n\n")

user = '{"user":{"name":"Husniddin", "age":18, "hobbies":["anime", "video games"]}}'
py_user = json.loads(user)
print(py_user["user"])
print(py_user["user"]["hobbies"])
print(type(py_user))

print("\n\n")

js_user = json.dumps(py_user)
print(js_user)
print(type(js_user))

print("\n\n")

nums = [1, 2, 3, 4]
print(nums)
print(type(nums))
js_nums = json.dumps(nums)
print(js_nums)
print(type(js_nums))



# RegEx -> Regular Expression

# Regex checks if a string contains the specified search pattern

# RegEx module re

import re

print("\n\n")

# search returns match object

txt = "Samarkand University of Technology"

# x = re.search("^Samarkand.*Technology$", txt)
x = re.search("\s", txt)

print(x.start())

if x:
    print("Yes it matches")
else:
    print("No match")

txt2 = "The rain in Spain and gain in spain"

# findall returns a list

xs = re.findall("ai", txt2)
print(xs)

# split returns list

xsplit = re.split(" ", txt2)
print(xsplit)

# sub replace and retunrs string

xsub = re.sub(" ", " this is sparta ", txt2)
print(xsub)


txt3 =  "HEllo WORLd hello!"

x2 = re.search("el", txt3, re.IGNORECASE)
x3 = re.search("el", txt3)

print(x2.start())
print(x3.start())

txt4 = "  a king,  a God,  a ..."
print(re.sub("  ", "I am not ", txt4))