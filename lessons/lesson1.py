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

def calc(num1=int(input("Enter a first number: ")), num2=int(input("Enter a second number: ")), operation=    input("Enter an operation: ")):
    if(operation == "+"):   print(num1+num2)
    elif(operation == "-"): print(num1-num2)
    elif(operation == "*"): print(num1*num2)
    elif(operation == "/"): print(num1/num2)

# calc()
calc(4, 2, "*")
# calc(num2=2, operation="/", num1=10)

# * takes the arguments which has no parameters

def list_users(admin, *users):
    print(admin)
    print(users)

list_users("husniddin", "nurmuhammad", "muhammad")
