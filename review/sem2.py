# a variable which is created inside function belongs to  local scope.
# a variable which is created in body of python program belongs to the global scope.

num = 10    # global scope

def func():
    num2 = 10 # local scope

def myfunc():
    global num3 
    num3 = 10

myfunc()
print(num3)

# import module as m 

# m.sayHi(m.user["name"])

from module import user as u

print(u["name"])

import platform

print(platform.system())
print(dir(platform))

# iterators

list1 = ["apple", "banana", "orange"]

list_iter = iter(list1)

print(next(list_iter))
print(next(list_iter))
print(next(list_iter))


# polymorphism

# many forms
# function,method, operators with same name but can be executed in many objects and classes.

# There 2 kinds of it.

# 1. compile-time p

# Decides which operator or method to run during copilation. often with method overloading.

# 2. runtime p

# overriding.
# behavior of method is decided while program is running, based on object it is calling.


# recursion is function calling itself until base problem is solved

# scope

# local->function

# global->program

x = 10

def func():
    global x
    x = 11
    print(x)

print(x)
func()
print(x)

# list, tuple, set, dictionary, string are iterable objects and they all have iter function which gives you iterator

list1 = {"key":"value","key1":"value","key2":"value",}
x=iter(list1)
print(next(x))
print(next(x))
print(next(x))

for i in list1:
    print(i)

