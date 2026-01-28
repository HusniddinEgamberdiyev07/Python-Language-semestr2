# low level -> binary code
# assembler level -> assembler
# high level -> c, c++, c#, python, java

# function based -> pascal, c
# oop -> c++, java, c#
# hybrid -> python

# def func_name(params):
#   statement

# parameter -> varaible name
# argument -> varaible value

def calc(num1=0, num2=0, operation=" "):
    if(operation == "+"):   print(num1+num2)
    elif(operation == "-"): print(num1-num2)
    elif(operation == "*"): print(num1*num2)
    elif(operation == "/"): print(num1/num2)

# calc(
#     int(input("Enter a first number: ")),
#     int(input("Enter a second number: ")),
#     input("Enter an operation: ")
# )

# calc(4, 2, "*")
# calc(num2=2, operation="/", num1=10)

# * takes the arguments which has no parameters

def list_users(admin, *users):
    print(admin)
    print(users)

list_users("husniddin", "nurmuhammad", "muhammad")

def loop_list(list):
    for item in list:
        print(item)

loop_list([1, 2, 3, 4])

def add(num1, num2):
    return  num1+num2

print(add(1, 2))

def multiplyBy5(x):
    return 5*x

print(multiplyBy5(2))

def dunno():
    pass

dunno()