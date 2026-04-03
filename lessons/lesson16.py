# permidation and combinations

# shuffle
# permutation

from numpy import random as r
import numpy as np

a = np.array([1,2])
print("before ", a)
r.shuffle(a)
print("after ", a)
r.shuffle(a)
print("after 1", a)
r.shuffle(a)
print("after 2", a)
r.shuffle(a)
print("after 3", a)

d = np.array([20,30])
print("before p ", d)

print("after p1 ", r.permutation(d))
print(d)

# shuffle changes orginal.
# permutation doe not change original it njust returns.