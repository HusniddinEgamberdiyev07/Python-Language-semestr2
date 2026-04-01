# Accessing array elements

# 1d array elements

import numpy as np

a1 = np.array([10,20,30, 40])
print(a1[3])
print(a1[1:3])
print(str(a1[1])+" "+str(a1[2]))

# access 2d array elements

# (row, column)
#       column
# row       |1   2|   1d array
# row       |3   4|

a2 = np.array([[1,2], [3,4]])
print(a2)

a3 = np.array([[1,2],[3,4]])

print(a3)
print(a3[0][0])
print(a3[0,0])
print(a3[0][1])
print(a3[1][0])

print(a3[1][0:2])
print(a3[1, 0:2])

a4 = np.array([
    [
        [1,2],
        [3,4]
    ],[
        [5,6],
        [7,8]
    ]
])

print(a4)
print(a4[0][0][0])
print(a4[0,0,0])
print(a4[1, 0, 1])
print(a4[1,1,1])

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

print(a[0,0]+b[0,0])

print("\n")

matrix = []

for i in range(0, len(a)):
    row = []
    for j in range(0, len(a[i])):
        row.append(a[i][j]+b[i][j])
    matrix.append(row)

print(np.array(matrix))

# for i,j in  [a, b]:
#     print(i, j)

# print([a,b])

# for i, j in a:
#     print(i, j)

# random numbers in python

from numpy import random

num = random.randint(-100, 0, 5)
num2 = random.rand(1)

num3 = random.randint(100, size=10)

print(num)
print(type(num))
print(num2)
print(num3)

num4 = random.randint(100, size=(3, 5))
print(num4)

num5 = random.rand(3,5)*100
print(num5)

x = random.uniform(100,900, (3,5))
print(x)