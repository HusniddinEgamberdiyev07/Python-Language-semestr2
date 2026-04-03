# numPy - numerical python
# it is a python library
# numPy is used to work with arrays, python itself does not have arrays
# It is open source and free

import numpy as np 

arr = np.array([1, 2, 3, 4, 5])

print(type(arr))
print(arr)
print(arr[0])
print(arr[2:])
arr[0] = 100
print(arr)

arr2 = arr[2:]
print(arr2)
arr2[0] = 1000
print(arr)

arr3 = np.array([x for x in range(1, 10)])
print(arr3)

arr4 = np.array((1, 2, 3, 5))
print(arr4)

# we have 0-d, 1-d and multi-d arrays
# every element on the array is called 0-d
# [1, 2, 3] we have three 0-d arrays

arr5  = np.array("hello")
print(arr5)
print(type(arr5))

# 1-d are the collection of 0-d arrays
arr6 = np.array([90, 80, 70])
print(arr6)

arr7 = np.array([10])
print(arr7[0])

# 2-d is collection of 1-d arrays

arr8 = np.array([["hello there", ], ["another one"]])
print(arr8[0][0])

# 3-d is collection 2-d
arr9 = np.array([[[1, 2],[3, 4]], [[5, 6], [7, 8]]])
print(arr9)
print(arr9.ndim)
print(arr9[0].ndim)
print(arr9[0][0].ndim)
print(arr9[0][0][0].ndim)

arr10 = np.array([[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]])
print(arr10.ndim)