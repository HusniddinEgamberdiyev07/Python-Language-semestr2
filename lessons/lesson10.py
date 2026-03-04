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

txt3 =  "HEllo WORLd hello!"

x2 = re.search("el", txt3, re.IGNORECASE)
x3 = re.search("el", txt3)

print(x2.start())
print(x3.start())

# findall returns a list

xs = re.findall("ai", txt2)
print(xs)

# split returns list

xsplit = re.split("\s", txt2) # \ is escape sequance. \s i space

[print(i) for i in xsplit ]

print("\n\n")
# sub replace and retunrs string

xsub = re.sub(" ", " this is sparta ", txt2)
print(xsub)

print("\n")

txt4 = "  a king,  a God, I am a ... human"
print(re.sub("\s\s", " I am not ", txt4).strip())

print("\n\n")

# -- Meta characters -- 

# [] -> they are container. Set of characters

something = re.sub("\s\s", " I am not ", txt4).strip()
print(re.findall("[a-z]", something))   # Lowercase letters
print(re.findall("[A-Z]", something))   # Uppercase letters

# \ -> signals or sequance

# \d -> digits

salary = "you made 89 dollars in 2 months"
print(re.findall("\d", salary))

# 5 length string start with he and ends with o
# hello
# heddo
# hebbo

# . any charcater is dot except new line

print("\n\n")

# hello = "Uzbekistanhellofromme"

hello = "The rain in Spaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaain"
# print(re.findall("he..o", hello))

# ^ -> starts with

if re.findall("^The", hello): print("starts with")
else: print("does not starts with")

# $ -> ends with

if re.findall("Spa*in$", hello): print("ends with")
else: print("does not ends with")


# * zero or more occurance

if re.findall("^The.*Spa*in$", hello): print("Does")
else: print("Does not")

star = "sn"
print(re.findall("s.*n", star))

# + one or more occurance
print(re.findall("s.+n", star))

# ? zero or one occurance

# text1 = "hello"
text1 = "helo"
print(re.findall("he.?o", text1))

# {} -> exactly specified occurance

text2 = "helllo"
print(re.findall("hel{3}o", text2))

text3 = "hello muhahhahahaha world"
print(re.findall("he.{2}o", text3))

# | -> either

print(re.findall("hello|world", text3))
print(re.findall("world|something", text3))

# \A -> starts with
txt4 = "The rain% in spain falls$ on plain9@"
print(re.findall("\AThe", txt4))

# \B -> start with or end with
print("\n\n")
print(re.findall(r"\bThe", txt4))
print(re.findall(r"\bplain", txt4))
print(re.findall(r"The\b", txt4))
print(re.findall(r"plain\b", txt4))

# \s -> space

print(re.findall("\s", txt4))

# \S -> no space characters

print(re.findall("\S", txt4))

# \w -> word characters [A-Z] [0-9]

print(re.findall("\w", txt4))

# \W -> no word characters

print(re.findall("\W", txt4))

# \Z -> ends with

print(re.findall("plain9@\Z", txt4))

# [] -> set, if one of them is there it will return

print(re.findall("[ai]", txt4))
print(re.findall("[a-n]", txt4)) # a to n

# [^ai] -> returns all character except a, i 

print(re.findall("[^ai]", txt4))
print(re.findall("[^a-z]", txt4))
print(re.findall("[^0-9]", txt4))
print(re.findall("[^a-zA-Z0-9\s]", txt4))
print(re.findall("[a-zA-Z]", txt4))
print(re.findall("[$@]", txt4))
print(re.findall("[+]", txt4))