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

## Date

### Creating date objects

```python
import datetime as dt

myBirthDay = dt.datetime(2007, 11, 12)
print(myBirthDay)
```

### now

```python
now = dt.datetime.now()
print(now)
```

### strftime

- **Weekday** - %a (short) %A (full) %w (number 0-6)
- **Month** - %b (short) %B (full) %m (number 01-12)
- **Year** - %y (short) %Y (full)
- **Day of the month (1-31)** - %d
- **Day of the year (1-366)** - %j
- **Hour (00-23)** - %H
- **Hour (00-12)** - %I
- **PM/AM** - %p
- **Minute** - %M
- **Second** - %S

## JSON (Javascript object notation)

From json to python. **json.loads()**

From python to json. **json.dumps()**

## RegEx (Regular Expression)

RegEx methods:

- **findall** - Returns all matches in a list.
- **search** - Returns first match in objcet.
- **split** - Returns list where string splitled at each match
- **sub** - replaces matches

```python
import re

text = "The rain in a spain"

print(re.findall("ai", text)) #['ai', 'ai']
print(re.search("ai", text)) # <re.Match object; span=(5, 7), match='ai'>
print(re.split("ai", text)) # ['The r', 'n in a sp', 'n']
print(re.sub("ai", "die", text)) # The rdien in a spdien
```

### Metacharacters:

- **.** - any
- **^** - starts with
- **$** - ends with
- **\*** - zero or more occurance
- **+** - one or more occurance
- **?** - zero or one occurance
- **{}** - exactly specified occurance
- **|** - or

### Special Sequences

- **\A** - returns match if characters at the beginning.
- **\b** - returns match if characters at the beginning or at the end.
- **\d** - returns match if string has digits
- **\s** - returns match if string has white spaces
- **\S** - returns match if string does not have white spaces
- **\w** - returns match if string has word character (a to z, 0-9, underscore )
- **\W** - returns match if string does not have word characters
- **\Z** - returns match if character is at the end of string

### Sets

- **[a-z]** - letters from a to z
- **[0-9]** - digits from 0 to 9
- **[^0-9]** - except from 0 to 9

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

### Deleting
 
Deleting file.

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

Generate random number from array elements.

```python
letters = np.array(["a", "b", "c", "d", "f", "h"])
print(r.choice(letters))
```
Generate an array with random elements from an array. Size tells what shape it should be.

```python
letters = np.array(["a", "b", "c", "d", "f", "h"])
print(r.choice(letters, size=(2,3)))
```

Generate an array with zeroes.

```python
zeroes = np.zeros((2,3))
print(zeroes)
```

Generate an array with the same number.

```python
sameNumArr = np.full((4, 2), 20)
print(sameNumArr)
```

Generate an array within a range

```python
from1To10 = np.arange(1,10)
print(from1To10)
```

### Array shape

Checking a shape of an array.

```python
arr = np.array([[1,2,3,4], [2,13,40, 10]])
print(arr.shape)
```

Changing array shape

```python
arr = np.array([[1,2,3,4], [2,13,40, 10]])
arr.shape = (4,2)
print(arr)
```

### Array sum

Sum all elements of arrays.

```python
nums1 = r.randint(1,100, size=2)
nums2 = r.randint(1,100, size=2)
print(nums1, "\n" , nums2)
print(np.sum([nums1, nums2]))
```

Sum column elements.

```python
print(np.sum([nums1, nums2], axis=0))
```

Sum row elements.

```python
print(np.sum([nums1, nums2], axis=1))
```



### Joining arrays

- **vstack** -> Joins arrays inside a array. They stay as an array.

```python
nums1 = r.randint(1,100, size=5)
nums2 = r.randint(1,100, size=5)
print(np.vstack([nums1, nums2]))
```

- **hstack** -> Combines them in a array.

```python
print(np.hstack([nums1, nums2]))
```

- **column_stack** -> Takes one element from each element and puts them in one row.

```python
print(np.column_stack([nums1, nums2]))
```

### Random data distribution

1 means value will always occur, 0 means it will never occur.
0.6 value has 60% chance to occur.
Sum of all probibilities must be 1.

```python
gacha = r.choice(["s", "a", "b"], p=[0.06, 0.14, 0.8], size=[2,60])
print(gacha)
```

### Randomly rearrange an array

- **Shuffle** -> changes original.

```python
nums = np.array([1,2,3])
r.shuffle(nums)
print(nums)
```

- **Permutation** -> Does not change original returns a new array.

```python
nums = np.array([1,2,3])
r.permutation(nums)
print(nums)
print(r.permutation(nums))
```

## Matplotlib

Installing -> **pip install matplotlib**

Importing and checking the version.

```python
import matplotlib as mpt

print(mpt.__version__)
```

### Drawing a line.

We can connect point using **plot** method. It takes two parameters. First one for x points and second one for y points.

```python
import matplotlib.pyplot as plt
import numpy as np

xPoints = np.array([0, 10])
yPoints = np.array([0, 15])

plt.plot(xPoints, yPoints)
plt.show()
```

### Without lines

```python
import matplotlib.pyplot as plt
import numpy as np

xPoints = np.array([0, 10])
yPoints = np.array([0, 15])

plt.plot(xPoints, yPoints, 'o')
plt.show()
```

### Many Points

```python
import matplotlib.pyplot as plt
import numpy as np
import numpy.random as r

xPoints = r.randint(1, 100, size=6)
yPoints = r.randint(1, 100, size=6)

plt.plot(xPoints, yPoints)
plt.show()
```

### Default xPoints

If we don't have xPonits matplotlib gives default ones such as 1,2,3,4 ...

```python
import matplotlib.pyplot as plt
import numpy as np
import numpy.random as r

yPoints = r.randint(1, 100, size=6)

plt.plot(yPoints)
plt.show()
```

### Multiple Lines.

```python
import matplotlib.pyplot as plt
import numpy as np
import numpy.random as r

yPoints = r.randint(1, 100, size=6)
yPoints2 = r.randint(1, 100, size=6)

plt.plot(yPoints)
plt.plot(yPoints2)
plt.show()
```

### Styling

Keywords:

- **marker**
- **markersize** - ms
- **markeredgecolor** - mec shorter variant
- **markerfacecolor** - mfc shorter variant
- **linestyle** - ls shorter variant
- **color** - changes line color. c is shorter variant
- **linewidth** - lw shorter variant.

```python
import matplotlib.pyplot as plt
import numpy as np
import numpy.random as r

yPoints = r.randint(1, 100, size=6)

# plt.plot(yPoints, marker="*", markersize=24, markeredgecolor="red", markerfacecolor="green", linestyle="dotted", color="orange", linewidth=10)
plt.plot(yPoints, marker="*", ms=24, mec="red", mfc="green", ls="dotted", c="orange", lw=10) # shorter variant
plt.show()
```

### Labels and title

- **xlabel**
- **ylabel**
- **title**

We can use **fondict={}** to change font styles for all three methods.

You can their position with **loc** parameter.
title->center, right, left
xlabel->center, right, left
ylabel->top, bottom, center

```python
import matplotlib.pyplot as plt
import numpy as np
import numpy.random as r

yPoints = r.randint(1, 100, size=6)


labelFont = {"size":20, "color":"blue", "family":"serif"}
titleFont = {"size":40, "color":"yellow", "family":"serif"}

plt.plot(yPoints, marker="o")
plt.title("Experiment", fontdict=titleFont, loc="right")
plt.xlabel("x nums", fontdict=labelFont, loc="left")
plt.ylabel("y nums", fontdict=labelFont, loc="bottom")
plt.show()
```

### Grid

We can add grids using **grid()** method.
We can use **axis** parameter to tell which lines to display. x, y and both.
We can also use **color**, **linestyle** and **linewidth** parameters.


```python
import matplotlib.pyplot as plt
import numpy as np
import numpy.random as r

yPoints = r.randint(1, 100, size=6)

plt.plot(yPoints, marker="o")
plt.grid(axis="y", linestyle="dotted", linewidth=5, color="brown")
plt.show()
```

### Display multiple plots

We can display mutiple plots using 

**subplot** method. It takes three parameters.

subplot(row, column, plotNum)

```python
import matplotlib.pyplot as plt
import numpy as np
import numpy.random as r

yPoints1 = r.randint(1, 100, size=10)
yPoints2 = r.randint(1, 100, size=10)

plt.subplot(2, 1, 1) # there are 2 rows and 1 column and this one is first plot
plt.plot(yPoints1)

plt.subplot(2, 1, 2)
plt.plot(yPoints2)

plt.show()
```

We can have title, xlabel, ylabel and grid for each plot. We have **suptitle** for all plots.

```python
import matplotlib.pyplot as plt
import numpy as np
import numpy.random as r

yPoints1 = r.randint(1, 100, size=10)
yPoints2 = r.randint(1, 100, size=10)


plt.subplot(2, 1, 1)
plt.plot(yPoints1)
plt.title("plot 1")
plt.xlabel("x nums plot1")
plt.ylabel("y nums plot1")
plt.grid(axis="x")

plt.subplot(2, 1, 2)
plt.plot(yPoints2)
plt.title("plot 2")
plt.xlabel("x nums plot2")
plt.ylabel("y nums plot2")
plt.grid(axis="y")

plt.suptitle("I am The Title")

plt.show()
```

### Scatter plots

```python
import matplotlib.pyplot as plt
import numpy as np
import numpy.random as r

xPoints = r.randint(1,100, size=16)
yPoints = r.randint(1,100, size=16)

plt.scatter(xPoints, yPoints, color="red")

xPoints2 = r.randint(1,100, size=16)
yPoints2 = r.randint(1,100, size=16)

plt.scatter(xPoints2, yPoints2, color="green")
plt.show()
```

We can color each dot with **c** parameter it takes list of colors.

```python
import matplotlib.pyplot as plt
import numpy as np
import numpy.random as r

xPoints = r.randint(1,100, size=5)
yPoints = r.randint(1,100, size=5)

plt.scatter(xPoints, yPoints, marker="*", c=["red", "green", "blue", "orange", "black"])
plt.show()
```
We can use colormap with **cmap** parameter. It is colorpallete. Values are from 1 to 100.
**colorbar** method shows colorbar.
We can give size for each point using **s** parameter. It takes list.
We can change transparency using **alpa** parameter from 1 to zero

```python
import matplotlib.pyplot as plt
import numpy as np
import numpy.random as r

xPoints = r.randint(1,100, size=15)
yPoints = r.randint(1,100, size=15)

colors = r.randint(1,100, size=15)
sizes = r.randint(10, 100, size=15)
randAlpha = r.rand(1)
plt.scatter(xPoints, yPoints, marker="*", c=colors, cmap="inferno", s=sizes, alpha=round(randAlpha[0], 1))
plt.colorbar()
plt.show()
```

### Bars

We can draw bar graphs using **bar** method.
We can create horizontal bars using **barh** method.

Parameters:
- **color**
- **width** - bar
- **hight** - barh

```python
import matplotlib.pyplot as plt
import numpy as np
import numpy.random as r

x = np.array(["A", "B", "C", "D"])
y = r.randint(20, 100, size=4)

plt.bar(x, y, color="red", width=0.6)
plt.show()
```

### Pie charts

**pie** method drwars it.
It is counterclockwise.

Parameters:
- **labels**-takes list.
- **startangle**-default 0.
- **colors**-takes list.
- **shadow**-True
- **explode**-takes list. If value 0 that element won't move if it is greater than 0 it moves.  

```python
import matplotlib.pyplot as plt
import numpy as np
import numpy.random as r

percentages = np.array([15, 35, 25, 25])
labels = np.array(["Banana", "Apple", "Orange", "Atom Bomb"])
myExplode = np.array([0,0,0,0.6])

plt.pie(percentages, labels=labels, startangle=180, shadow=True, explode=myExplode)
plt.legend(title="Three fruits with A bomb")
plt.show()
```