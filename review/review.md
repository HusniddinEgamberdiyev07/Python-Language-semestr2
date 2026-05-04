# Python review semestr 2.

## String formatting

```python 
name = "Husniddin"
age = 18
price = 45.752863
product = "apple"

msg = "Hello {0}. {0} is {1} years old. Paid {2:.2f} for {productName}"

print(msg.format(name, age, price, productName=product))
```

## PIP

PIP ( Preferred installer program ) is package manager.

pip --version -> checks do u have pip or not.

### Virtual enviroment

**Create:**

python -m venv folderName(usually venv)

**Activate:**

source venv/bin/activate

## Error handling

### Syntax

**try** -> test a block of code for an error.

**except** -> lets u handle an error. We can have many excepts with different exceptions

**else** -> lets u execute code when ther is no error.

**finally** -> lets u execute code whether you have error or not.

### Common types of Exceptions

- **ZeroDivisionError** -> Dividing number by zero.
- **ValueError** -> Incorrect argument for a function parameter. int("hello world")
- **TypeError** -> Applying operation to the wrong type. '2'+2
- **IndexError** -> Trying access list item which does not exist. [1,2][10]
- **KeyError** -> Trying to use a key which dictionary does not have. {}["name"]
- **FileNotFoundError** -> Trying to open file which does not exist.
- **NameError** -> Using variable which is not defined yet.

### Raise exception

To throw exception we can use raise keyword.

### Custom exceptions

We can create our custom exceptions by inheriting Exeception class.

### Examples

```python
try:
    print(a)
except NameError:
    print("No variable")
else:
    print("Success")
finally:
    print("I don't care")
```
Many excepts

```python
try:
    a=10
    print(a/0)
except NameError:
    print("No variable")
except:
    print("Something else went wrong")
else:
    print("Success")
finally:
    print("I don't care")
```

Custom exceptions & raising exception.

```python 
class TooLong(Exception):
    pass

try:
    name = input("Enter your name: ")
    if len(name) >= 10:
        raise TooLong("Name is too long")
except TooLong:
    print("Your name is too long. It should contain maximum ten chars.")
else:
    print(f"Welcome {name}")
```

## File handling

### File modes:

- **r** -> Read. Throws an error if file does not exist.
- **a** -> Append. Writes at the end of the file. Creates a new file if it does not exists.
- **w** -> Write. Deletes all data and writes. Creates a new file if it does not exists.
- **x** -> Create. Returns an error if file exist.
- **t** -> Text mode.
- **b** -> Binary mode.
- **+** -> Read and write

We can have combination of them: rb, wt, ab, w+ (erases the file), r+ (does not erases the file)

### Opening files.

We can open file with build in open funstion. It takes two parameters fileLocation and mode.

```python
file = open("./files/text.txt", "rt")
print(file.read()) # .read() shows the content of data
file.close() # closes files
```

Better way opeing file is **with**. It will close it automatically.

```python
with open("./files/text.txt", "rt") as file:
    print(file.read())
```

### File object attributes:

```python
with open("./files/text.txt", "rt") as file:
    print(file.name)
    print(file.mode)
    print(file.encoding)
    print(file.closed)
    print(file.read())
print(file.closed)
```

### Writing files.

```python 
userName = input("Enter your name: ")

with open("./files/userName.txt", "wt") as file:
    file.write(f"Users name is: {userName}")
```

### Reading files.

```python
with open("./files/userName.txt", "rt") as file:
    print(file.read()) # read all content.

with open("./files/userName.txt", "rt") as file:
    print(file.read(10)) # read first ten character.

with open("./files/userName.txt", "rt") as file:
    print(file.readline()) # read one line

# Reading line by line using loop.

with open("./files/userName.txt", "rt") as file:
    for line in file:
        print(line)
```

### Write to an existing file.

```python
userName = input("Enter your name: ")

with open("./files/userName.txt", "at") as file:
    file.write(f"Users name is: {userName}\n")
```

### Create new file.

```python
f = open("./files/newFile.txt", "x") # creates new file. Throws error if it exists.
f = open("./files/newFile.txt", "w") # creates new file if it does not exists.
f = open("./files/newFile.txt", "a") # creates new file if it does not exists.
```

### Deleting file.

```python
import os
os.remove("./files/newFile.txt") # removes file
```

Deleting empty folder.

```python
import os
os.rmdir("./empty")
```

Deleting non empty folder

```python
import shutil

shutil.rmtree("./nonEmpty")
```

## NumPy (Numerical Python)

### Creating arrays

We can pass lists, tuples, sets to array method and it convert them into **ndarray**

```python
import numpy as np

arr1 = np.array({1,2,3,4})
print(arr1)
```

### Array dimensions

- **0d array** -> Elements in the array.

```python
zeroD = np.array(1)
print(zeroD)
```

- **1d array** -> Is collections of 0d arrays.

```python
oneD = np.array([1,2,3])
print(oneD)
```

- **2d array** -> Is collection od 1d arrays.

```python
twoD = np.array([[1,2], [3,4]])
print(twoD)
```

We can check what dimension they are using **ndim** attribute.

```python
print(zeroD.ndim)
print(twoD.ndim)
print(oneD.ndim)
```

### Access array elements.

We can access array elements using their indexes.

```python
print(oneD[0])
print(twoD[1,0])
```

### Random numbers.

Random number from 0 to 100

```python
from numpy import random as r

randNum = r.randint(100)
print(randNum)
```

Generate 1d array which has 5 random numbers from 1 to 100.

```python
randArr1D = r.randint(100, size=5)
print(randArr1D)
```

Generate 2d array with 3 rows and which has 5 random numbers from 1 to 100

```python
randArr2D = r.randint(100, size=(3,5))
print(randArr2D)
```

Generate 1d array which has 5 random float numbers.

```python
randArr1DFloat = r.rand(5)
print(randArr1DFloat)
```

Generate 2d array with 3 rows and which has 5 random float numbers

```python
randArr2DFloat = r.rand(3,5)
print(randArr2DFloat)
```

Generate 2d array with 3 rows and which has 5 random float numbers from 1 to 100

```python
randArr2DFloat = r.rand(3,5) * 100
print(randArr2DFloat)
```