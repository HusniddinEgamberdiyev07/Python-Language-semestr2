# pip -> package installer program

# pip is package manager
# package is python module

# import camelcase as cc
# camelCase = cc.CamelCase()
# print(camelCase.hump("hello world"))

# pip install modulename
# pip uninstall modulname
# pip list



# Exception handling

# Try -> test the code for error.
# Except -> lets you handle an error.
# Else -> lets you execute code when there is no error.
# Finally -> lets you execute code, and does not care about try and except.

# when we have an error we will have exceptions.

# try:
#   all of my code
# except:
#   run when error happens
# else:
#  run when no error
# finally:
#   I don't care about try or except

try:
    # print(10/0) # ZeroDivisionError
    # print(x)  # NameError
    # print("a"/2)  # TypeError
    # int("abc")  # ValueError
    # a = [1, 2][2]  # IndexError
    # user = {}["key"]    # KeyError
    open("something.txt", "r")   # FileNotFoundError
    # print(f.read())
except NameError:
    print("Name error")
except TypeError:
    print("Type  error")
except ZeroDivisionError:
    print("You can't delete by zero")
except ValueError:
    print("Value error")
except IndexError:
    print("IndexError")
except KeyError:
    print("KeyError")
except FileNotFoundError:
    # raise Exception("File not found")
    print("FileNotFoundError")
else: 
    print("No error")
finally:
    print("I am working....")

# try:
#     num  = int(input())
#     res = 10/num
#     print(res)
# except ZeroDivisionError:
#     print("Enter non zero num")
# except ValueError:
#     print("Enter a number")

try:
    f = open("./lessons/lesson1.py", "r")
except FileNotFoundError:
    print("File error")
else:
    print("Success")
finally:
    print("I am finally")
    f.close()

# x=-1
# if x < 0:
#     raise ValueError("Negative value...")

# x=-1
# if x < 0:
#     raise Exception("Negative value...")


# si=(P*T*R)/100

# base money - P
# time - t
# rate of interest - r

class InvalidInputError(Exception):
    pass

def calc_simple_interest():
    try:
        p = float(input("p: "))
        t = float(input("t: "))
        r = float(input("r: "))

        if p<= 0 or r <= 0 or t <= 0:
            raise InvalidInputError("P,t,r must be greater than zero")
    except InvalidInputError as e:
        print(e)
    except ValueError:
        print("Value error")
    else:
        interest = (p*r*t)/100
        print(interest)

# calc_simple_interest()