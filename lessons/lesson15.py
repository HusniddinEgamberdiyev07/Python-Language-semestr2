# random numbers in python

import numpy as np
from numpy import random as r
import re

num = r.randint(-100, 0, 5)
num2 = r.rand(1)

num3 = r.randint(100, size=10)

print(num)
print(type(num))
print(num2)
print(num3)

num4 = r.randint(100, size=(3, 5))
print(num4)

num5 = r.rand(3,5)*100
print(num5)

x = r.uniform(100,900, (3,5))
print(x)

# choice takes array as a parameter

print("\n")

array1 = np.array(["hi", "bye", "go somewhere"])
print(r.choice(array1))
print(r.choice(array1, size=(3,5)))

array2 = np.array([10,20,30,40,50])
print(r.choice(array2, size=(4,8)))

print("\n")

# zero matrix

print(np.zeros((2,3)))

# matrix wiht my numbers

print(np.full((3,10), 10))

array3 = np.arange(10,21,2)
print(array3)

array4 = r.randint(1, 10, 10)
print(array4)

array5 = np.array([[1,2,100], [20,3,10]])
print(array5.shape)
print(array5.ndim)
array5.shape=(3,2)
print(array5)

print("\n")

n1 = np.array([20,40,30])
n2 = np.array([1,2,4])
n3 = np.array([0,10,40])

# adding everything
print(np.sum([n1, n2]))
print(np.sum([1,2,3]))
print(n1.sum())

# adding columns
print(np.sum([n1, n2, n3],axis=0))
# adding rows
print(np.sum([n1, n2, n3],axis=1))

# joining arrays
# vstack - vertical
# hstack - horizontal
# columns_stack

print("\n")

a1 = np.array([1,2,3])
a2 = np.array([10,20,30])
a3 = np.array([100, 200, 300])

print(np.vstack((a1, a2, a3)))  # rows

print(np.hstack((a1,a2)))   # all
print(np.hstack([a2,a1]))

print(np.column_stack([a1,a2,a3]))  # columns

x = r.choice(["*6","*5","*4"], p=[0.006, 0.2, 0.794], size=100)

print(x)