# matplotlib - graphs, charts

import matplotlib.pyplot as plt
import numpy as np

# print(matplotlib.__version__)

# pyplot is sub module of matplotlib

# 4 quadrant is what computer shows

# to draw a line we need starting and ending x and y pairs

# plot() draws a line
# param one is points of x
# param two is points of y

# x = np.array([5, 20, 20, 5, 5, 5, 20])
# y = np.array([5, 5, 25, 25, 5, 15, 15])
# x = np.array([10, 20, 20, 10, 10])
# y = np.array([-80, -80, 40, 40, -80])

# x2 = np.array([5, 25, 25, 5, 5])
# y2 = np.array([40, 40, 100, 100, 40])

# x3 = np.array([10, 20, 20, 10, 10])
# y3 = np.array([100, 100, 400, 400, 100])

# x4 = np.array([10, 20, 20, 10])
# y4 = np.array([400, 400, 700, 400])

# x = np.array([0, 0, 0, 10, 10,5, 10, 10]) #mess
# y = np.array([10, 15, 10, 10, 20,20, 10])


# plt.plot(x, y)
# plt.plot(x, y, "o")
# plt.plot(x, y, marker="o")
# plt.show()

# x = np.array([0, 5, 10, 20, 20, 30])
# y = np.array([0, 5, 0, 15, 5, 30])

# x = np.array([0, 30])
# y = np.array([20, 20])

# plt.plot(y, marker="o")
# plt.plot(x, y, marker="o")

# plt.plot(x, y, marker="o")
# plt.plot(x, y, marker="1")
# plt.plot(x, y, marker="2")
# plt.plot(x, y, marker="3")
# plt.plot(x, y, marker="3")

# plt.plot(x, y, ms="10", marker="o")
# plt.plot(x2, y2, ms="10", marker="o")
# plt.plot(x3, y3, ms="10", marker="o", color="blue")
# plt.plot(x4, y4, ms="10", marker="o", color="blue")

# fmt
# marker|line|color

# titleFont = {"family":"Cantarell Extra Bold", "color":"blue", "size":"20", "weight":"bold"}
# labelFont = {"family":"serif", "color":"red", "size":15}

# plt.xlabel("x-axis", fontdict=labelFont, loc="left")
# plt.ylabel("y-axis", fontdict=labelFont, loc="bottom")
# plt.title("Something", fontdict=titleFont, loc="right")

# plt.grid()

# plt.subplot(1, 1, 1)
# plt.plot(np.array([5, 30]), np.array([10, 10]), "h--k", ms=25, markeredgecolor="red", mfc="blue")

# plt.subplot(2, 1, 2)
# plt.plot(np.array([5, 30]), np.array([20, 20]), "h--k", ms=25, markeredgecolor="red", mfc="blue")

# plt.subplot(1, 3, 3)
# plt.plot(np.array([5, 30]), np.array([30, 30]), "h--k", ms=25, markeredgecolor="red", mfc="blue")
# plt.show()
# mec - markeredgecolor
# mfc - inside marker

# linestyle - ls
# linewidth - lw


# plt.plot(x,y, ls="dashdot", color="black", marker="o", ms=20, mfc="blue", mec="green", lw=10)

# plt.grid(axis="x")
# plt.grid(axis="y")
# plt.grid(color="green", ls="--", lw=3)

# plt.show()

# subplot(row, column, whichPLot)


# x = np.array([0, 10])
# y = np.array([5, 5])


# plt.subplot(1,3,1)
# plt.plot(x, y)
# plt.title("something1")
# plt.grid()

# x2 = np.array([0, 10])
# y2 = np.array([5, 10])

# plt.subplot(1,3,2)
# plt.plot(x2,y2)
# plt.title("something2")


# x3 = np.array([0, 15, 15])
# y3 = np.array([5, 10, 0])

# plt.subplot(1,3,3)
# plt.plot(x3,y3)
# plt.title("something3")
# plt.grid()

# plt.suptitle("something The Great")

# plt.show()

# x = np.array([0, 10])
# y = np.array([5, 5])

# plt.subplot(3,1,1)
# plt.plot(x, y)

# x2 = np.array([0, 10])
# y2 = np.array([5, 10])

# plt.subplot(3,1,2)
# plt.plot(x2,y2)

# x3 = np.array([0, 15, 15])
# y3 = np.array([5, 10, 0])

# plt.subplot(3,1,3)
# plt.plot(x3,y3)

# plt.show()


array1 = np.array([5,6,7,8, 6])
array2 = np.array([5,6,7,8, 5])

colors = np.array(["red", "blue", "green", "purple", "orange"])

# colors = np.array([100,20,30,40,0])
# sizes = np.array([70,20,100,30,5])

# array3 = np.array([9,1,7,8, 6])
# array4 = np.array([5,6,2,2, 10])

randArr1 = np.random.randint(1500, size=1500)
randArr2 = np.random.randint(1500, size=1500)
colors = np.random.randint(100, size=1500)
sizes = np.random.randint(100, size=1500)*10
a = np.random.randint(101, size=1500)/100

# plt.scatter(array1, array2, c=colors)
# plt.scatter(array1, array2,cmap="viridis", c=colors, s=sizes, alpha=0.1)
# plt.scatter(array3, array4, color="purple")

# plt.scatter(randArr1, randArr2,cmap="nipy_spectral", c=colors, s=sizes, alpha=a)

plt.suptitle("Scatter")
plt.xlabel("x", fontdict={"color":"red"}, loc="left")
plt.ylabel("y", fontdict={"color":"blue"}, loc="bottom")
# plt.grid(ls="dashed")
# plt.colorbar()
# plt.cool()

# plt.show()

names = np.array(["Me", "You", "He", "Extra"])
marks = np.array([99, 2, 89, 0])

# plt.bar(randArr1, randArr2, color="brown", width=2)
# plt.show()

names = ["Husniddin", "Husan", "Sardor", "Extra", "Extra2"]
marks =[10,20,30, 25, 90]
colors2 = ["red", "green", "blue"]
widths = [0.1, 0.2, 1.2]
# plt.barh(names, marks, color = colors2, height=widths)

nums = np.random.normal(170, 10,250)
# plt.hist(nums)
# plt.show()

plt.pie(marks, labels=names, startangle=90, counterclock=False, explode=[0.2,1,0.2,0.2,0.2], shadow=True, colors=["gold","brown", "red", "blue", "orange"])
plt.legend(loc="lower left", title="Names")
plt.show()