# try:
#     a=10
#     print(a/0)
# except NameError:
#     print("No variable")
# except:
#     print("Something else went wrong")
# else:
#     print("Success")
# finally:
#     print("I don't care")


# class TooLong(Exception):
#     pass

# try:
#     name = input("Enter your name: ")
#     if len(name) >= 10:
#         raise TooLong("Name is too long")
# except TooLong:
#     print("Your name is too long. It should contain maximum ten chars.")
# else:
#     print(f"Welcome {name}")


name = "Husniddin"
age = 18
price = 45.752863
product = "apple"

msg = "Hello {0}. {0} is {1} years old. Paid {2:.2f} for {productName}"

print(msg.format(name, age, price, productName=product))

file = open("./files/text.txt", "rt")
print(file.read()) # .read() shows the content of data
file.close() # closes files

with open("./files/text.txt", "rt") as file:
    print(file.name)
    print(file.mode)
    print(file.encoding)
    print(file.closed)
    print(file.read())
print(file.closed)

# userName = input("Enter your name: ")

# with open("./files/userName.txt", "at") as file:
#     file.write(f"Users name is: {userName}\n")

with open("./files/userName.txt", "rt") as file:
    print(file.read()) # read all content.

with open("./files/userName.txt", "rt") as file:
    print(file.read(10)) # read first ten character.

with open("./files/userName.txt", "rt") as file:
    print(file.readline()) # read one line

# Reading line by line using loops.

with open("./files/userName.txt", "rt") as file:
    for line in file:
        print(line)

# f = open("./files/newFile.txt", "x") # creates new file. Throws error if it exists.
# f = open("./files/newFile.txt", "w") # creates new file if it does not exists.
# f = open("./files/newFile.txt", "a") # creates new file if it does not exists.

# import os
# os.remove("./files/newFile.txt") # removes file
# os.rmdir("./empty")

# import shutil

# shutil.rmtree("./nonEmpty")

import numpy as np

arr1 = np.array({1,2,3,4})
print(arr1)

oneD = np.array(1)
print(oneD)

twoD = np.array([1,2,3])
print(twoD)

threeD = np.array([[1,2], [3,4]])
print(threeD)

print(threeD.ndim)
print(twoD.ndim)
print(oneD.ndim)

print(twoD[0])
print(threeD[1,0])

from numpy import random as r

randNum = r.randint(100)
print(randNum)

randArr1D = r.randint(100, size=5)
print(randArr1D)

randArr2D = r.randint(100, size=(3,5))
print(randArr2D)

randArr1DFloat = r.rand(5)
print(randArr1DFloat)

randArr2DFloat = r.rand(3,5) * 100
print(randArr2DFloat)

# something = open("./files/something.txt", "w")
# something = open("./files/something.txt", "r+")
# something.write("Welcome to this hellish worldewfeq")
# print(something.read())
# something.close()

# with open("./files/something.txt", "a+") as file:
#     file.write("Hello world\n")
#     file.seek(0)
#     print(file.read())

randNum3D = r.randint(1, 100, size=(3, 2, 10))
print(randNum3D)

randNumFloat3D = r.rand(3,2,10)*100
print(randNumFloat3D)

letters = np.array(["a", "b", "c", "d", "f", "h"])
print(r.choice(letters))
print(r.choice(letters, size=(2,3)))

zeroes = np.zeros((2,3))
print(zeroes)

sameNumArr = np.full((4, 2), 20)
print(sameNumArr)

from1To10 = np.arange(1,10)
print(from1To10)

arr = np.array([[1,2,3,4], [2,13,40, 10]])
arr.shape = (4,2)
print(arr)

nums1 = r.randint(1,100, size=5)
nums2 = r.randint(1,100, size=5)
print(nums1, "\n" , nums2)
print(np.sum([nums1, nums2]))
print(np.sum([nums1, nums2], axis=0))
print(np.sum([nums1, nums2], axis=1))

nums1 = r.randint(1,100, size=5)
nums2 = r.randint(1,100, size=5)

print(np.vstack([nums1, nums2]))
print(np.hstack([nums1, nums2]))
print(np.column_stack([nums1, nums2]))

gacha = r.choice(["s", "a", "b"], p=[0.06, 0.14, 0.8], size=[2,60])
print(gacha)

nums = np.array([1,2,3])
r.permutation(nums)
print(nums)
print(r.permutation(nums))