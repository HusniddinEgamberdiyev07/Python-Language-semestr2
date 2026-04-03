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


# plt.plot(x, y)
# plt.plot(x, y, "o")
# plt.plot(x, y, marker="o")
# plt.show()

# x = np.array([0, 5, 10, 20, 20, 30])
# y = np.array([0, 5, 0, 15, 5, 30])

x = np.array([5, 30])
y = np.array([20, 20])

# plt.plot(y, marker="o")
# plt.plot(x, y, marker="o")

# plt.plot(x, y, marker="o")
# plt.plot(x, y, marker="1")
# plt.plot(x, y, marker="2")
# plt.plot(x, y, marker="3")
# plt.plot(x, y, marker="3")

# plt.plot(x, y, marker="s", markersize=20, color="gold")
# fmt
# marker|line|color

plt.plot(x, y, "h--k", ms=25, markeredgecolor="red", mfc="blue")

# mec - markeredgecolor
# mfc - inside marker

plt.show()
