# 61-103

# module is just a python file and  we can import hem using import statement.
# we can access modules functions and varibales.
# we can rename module using as.

import module as m

print(m.user)

m.sayHi(m.user["name"])

# python has a lot of built in modules we can import them without installing them.

# platform is a built in module

import platform

# print(dir(platform))

# print(platform.platform())

# dir lists all functions and it is built in function.

# we can import parts of code using from keyword.
# from modulName import part

from module2 import sum as s

s(10, 20)





# datetime is a built in module

# current date

import datetime as d

now = d.datetime.now()

print(now)

# date contains year, month, day, hour, minute, second, microsecond

# creating a date object

dateBirth = d.datetime(2007, 12, 11)
print(now-dateBirth)

# datetime takes hour., minute, second, microsend, tzone parameters
# they are optional and 0 by default and tzone is none by default

# strftime to format datetime it takes one parameter

# weekday

# %a - short version
# %A - long version
# %w - as a number

print()

print(now.strftime("%a"))
print(now.strftime("%A"))
print(now.strftime("%w"))

# month 

# %b - short version
# %B - long version
# %m - as a number

print()

print(now.strftime("%b"))
print(now.strftime("%B"))
print(now.strftime("%m"))

# day of month as a number

print()

print(now.strftime("%d"))

# year

# %y - short version
# %Y - long version

print()

print(now.strftime("%y"))
print(now.strftime("%Y"))

# hour 

# %H - 00-23
# %I - 00-12
# %p - AM-PM

print()

print(now.strftime("%H"))
print(now.strftime("%I"))
print(now.strftime("%p"))

# minute 00-59

print()

print(now.strftime("%M"))

# second 00-59

print(now.strftime("%S"))

# day of the year 1-366

print()

print(now.strftime("%j"))


print()

# hours 00-12, minute, second, day of the year, year
print(now.strftime("Hours: %I, Minutes: %M, Seconds %S, Day of the year: %j, Year: %Y"))





# Math is a built in module

# We have got bulit in python math functions

# min and max functions returns minimum or maximum

print()

print(min(2, 20, 3))
print(max(2, 20, 3))

# pow(num, power) num**power

print()

print(4**3)
print(pow(4, 3))

# abs - absolute value

print()

print(abs(-5))

# round - rounds number to the closest and second param is how many digits after dot

print(round(4.6))
print(round(4.8190279402, 2))

# math module

import math as mth

# sqrt - square root

print(mth.sqrt(9))

# ciel - round up
# floor - round down

print(mth.floor(4.6))
print(mth.ceil(4.3))

# pi

print(mth.pi)




# Json (Javascript Object Notation)

# Usage:

# Data share (Rest apis)
# Configuration files (vs code)
# Data storage (Mongodb)
# Web development

# Why json:

# Works well with  near all languages
# Easy to parse
# Readable
# Flexible
# Lightweight

# python has build in package json

import json

print()

# json -> python 
# json.loads(json)

# python -> json
# json.dumps(python)

jsonStr = '{ "name":"John", "age":30, "city":"New York"}'
jsonPy = json.loads(jsonStr)

print(jsonPy)
print(type(jsonPy))

dict1 = {"names":["Husniddin", "Muxammad", "Nurmuhammad"]}
pyJson = json.dumps(dict1)

print(pyJson)
print(type(pyJson))




# Regex - regular expression
# used for search patterns

# It is a built in package

print()

import re

# findall - returns list of matches.
# search - returns firts match as an object.
# sub - replaces matches
# split - returns splitted list

sentence = "Hello world Hate world Destroy world" 

print(re.findall("world", sentence), "\n")

print(re.search("world", sentence))
print(re.search("world", sentence).start())
print(re.search("world", sentence).end(), "\n")

print(re.sub("world", "something", sentence), "\n")

print(re.split("world", sentence))
print(re.split("o", sentence), "\n")

# Metacharacters:

text0 = "username:Husniddin;"

# . - any character
# ^ - starts with
# $ - ends with

print(re.findall(":.*;$", text0), "\n")

print(re.search(r"(\w+):(\w+);", text0).group(0))
print(re.search(r"(\w+):(\w+);", text0).group(1))

print(re.findall("^username", text0))
print(re.findall(";$", text0), "\n")


text = "Helllo helo hellllo heo"

# * - zero or more occurance
# + - one or more occurance
# ? - zero or one occurance
# {} - specified occurance

print(re.findall("hel*o", text))
print(re.findall("hel+o", text))
print(re.findall("hel?o", text))
print(re.findall("hel{4}o", text))

# () - grouping

date1 = "12-11-2007"
pattern = "mm-dd-yyyy"

print(pattern, re.search("([0-9]{2})-([0-9]{2})-([0-9]{4})", date1).group())
print(pattern, re.search("([0-9]{2})-([0-9]{2})-([0-9]{4})", date1).group(1))
print(pattern, re.search("([0-9]{2})-([0-9]{2})-([0-9]{4})", date1).group(2))
print(pattern, re.search("(?P<mm>[0-9]{2})-([0-9]{2})-(?P<yyyy>[0-9]{4})", date1).group("yyyy"))
print(pattern, re.search("(?P<mm>[0-9]{2})-(?P<dd>[0-9]{2})-(?P<yyyy>[0-9]{4})", date1).groupdict())


text = "Send mail to alice@gmail.com or bob.smith@company.org for help. husniddin200708@gmail.com"
# Output: ['alice@gmail.com', 'bob.smith@company.org']
# print(re.findall(r"[a-zA-z0-9.]+@[a-zA-z.]+", text))
print(re.findall(r"[\w.]+@[\w.]+", text))
print(re.search(r"([\w.]+)@[\w.]+", text).group(1))

text2 = "Alice went to New York on Monday"

print(re.findall("[A-Z][a-zA-z]+", text2))

text3 = "Loving #Python and #regex today! #100DaysOfCode"

print(re.findall("#[a-zA-Z0-9]+", text3))

text4 = "Visit https://google.com or http://example.org/page?q=1 for more."
# Output: ['https://google.com', 'http://example.org/page?q=1']

print(re.findall("(?:https|http)://[a-zA-Z0-9_.?=/]+", text4))

text5 = "[ERROR] 2024-01-15 12:03:44 - Disk full"
# Output: level='ERROR', date='2024-01-15', time='12:03:44', message='Disk full'

searched = re.search(r"\[(?P<level>[A-Z]+)\] (?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}:\d{2}) - (?P<message>[a-zA-Z ]+)", text5)

print(f"Level {searched.group("level")} date {searched.group("date")} time {searched.group("time")} message {searched.group("message")}")