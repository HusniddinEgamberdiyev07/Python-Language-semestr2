price = 49.99999999999
orders = 3
text = "This costs {0:.2f}$ and you ordered {0:.2f}"
print(text.format(price, orders))
text2 = "This costs {1:.2f}$ and you ordered {0:.2f}"
print(text2.format(price, orders))

print("\n\n")

# -- File handling --
import re

# Python has built in module for file handling

# We can read, open, close, update, write files

try:
    f = open("./lessons/something.txt", "rt")
except FileNotFoundError:
    print("Not found")
else: 
    print(f.read())
    f.close()

# we close the file to save changes, clear the memory, protect data ingetrity and prevent access problems

print('\n\n')

try:
    with open("./lessons/something.txt", "r+") as f:
        content = f.read()
        print(content)
        print(f.name)
        print(f.mode)
        print(f.closed)
        print(f.encoding)
    print(f"{f.closed} is close")

except FileNotFoundError:
    print("Not found")

# name = input("enter your name")

# with open("./lessons/users.txt", "w") as f:
#     f.write(f"name: {name}")

# with open("./lessons/users.txt", "r") as f:
#     print(f.read())

# P = input("Enter p")
# I = input("Enter i")
# R = input("Enter r")

# with open("./lessons/variables.txt", "a") as f:
#     f.write(f"p:{P}i:{I}r:{R}")

print("\n\n")

list1 = []

try:
    with open("./lessons/variables.txt", "r") as f:
        content = f.read()
        
        for i in range(0, len(re.findall(":[0-9]*", content))):
            num = re.findall(":[0-9]*", content)[i][1:]
            key = re.findall("[a-zA-Z]", content)[i]

            list1.append({
                "key":key,
                "num":int(num)
            })
            
        print(list1)
        # print(content)

except FileNotFoundError:
    print("Not found")

if len(list1)>0:
    p = 0
    i = 0
    r = 0

    for index in range(0, len(list1)):
        if list1[index]["key"] == "p":
            p = list1[index]["num"]
        elif list1[index]["key"] == "i":
            i = list1[index]["num"]
        elif list1[index]["key"] == "r":
            r = list1[index]["num"]

        if (index + 1) % 3 == 0 and index != 0:
            sc = (p*i*r)/100
            # print(p)
            # print(i)
            # print(r)
            print(sc)


# name = input("Enter your name: ")

# with open(f"./lessons/users/{name}.txt", "w") as userFile:
#     userFile.write(f"name:{name},")

# with open(f"./lessons/users.txt", "w") as userFile:
#     userFile.write(f"name:{name},")

# def save_user_profile():
#     name = input("Enter your name: ")
#     age = int(input("Enter your age: "))
#     email = input("Enter your email: ")

#     with open(f"./lessons/users_profile.txt", "a") as f:
#         f.write("=== User profile ===\n")
#         f.write(f"Name:{name}\n")
#         f.write(f"Age:{age}\n")
#         f.write(f"Email:{email}\n")

#         print("Saved")

# to write some info on file we use write method
# to read use read

print("\n\n")

# name = input("Name: ")

# with open("./lessons/names.txt", "a") as f:
#     f.write(f"{name}\n")

# with open("./lessons/names.txt", "r") as f:
#     names = f.readlines()
    
# print("Names: ")
# for name in names:
#     print(name.strip())



# with open("./lessons/names.txt", "r") as f:
#     names = f.read()
    
# print(names)
# print("Names: ")
# for name in names:
#     print(name.strip())

import os
import shutil

with open("./lessons/names.txt", "r") as f:
    # print(f.readline())
    # print(f.readline())
    # print(f.readline())

    for line in f:
        print(line.strip())
    if f.readline() == "":
        print("The end")

try:
    open("./lessons/names.txt", "x")
except FileExistsError:
    print("It is already there")

# os.remove("./lessons/names2.txt") # delete this file
# os.remove("./lessons/hello/something.txt")
# os.rmdir("./lessons/hello")
# os.mkdir("./lessons/hello")
# shutil.rmtree("./lessons/hello")