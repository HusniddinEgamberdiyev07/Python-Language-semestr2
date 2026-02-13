# -- Polymorphism --

# polymorphism is changing methods behiover accoring to situation.
# There are two types of polmorphism

# 1) compile-time -> it happens when we press run button ( method overloading )
# It choose which method it needs to use during compile-time


# 2) runtime ( method overriding )
# It happens during run time

class Vehicle:
    def __init__(self, brand, cost):
        self.brand = brand
        self.cost = cost

    def move(self):
        print("Moving! "+self.brand)

class Car(Vehicle):
    pass

    # def move(self):
    #     print("Drive! "+self.brand)

class Boat(Vehicle):
    def move(self):
        print("Sail! "+self.brand)

class Plane(Vehicle):
    def move(self):
        print("Fly! "+self.brand)


car1 = Car("bmw", "10000$")
boat1 = Boat("yacht", "15000$")
plane1 = Plane("boing", "100000$")

for obj in (car1, boat1, plane1):
    print(obj.brand)
    print(obj.cost)
    obj.move()
    print("")


# -- Scope -- 

# Scope is how much you can see

# We have two scopes:
# 1) local scope
# Variables inside function. Only that function can access it.

# 2) Global scope
# Everything can access global.

def sayHI():
    name = "Husniddin"

    print(name)

sayHI()

# print(name) -> error name is local variable

def showMsg():
    global msg  # we are telling it is not local
    msg = "Hello World"
    print(msg)

showMsg()
print(msg)  # no error

# scope goes from local to global

num = 100
def showNum():
    num = 10
    print(num)
showNum()
print(num)

num2 = 25

def showNum2(): 
    print(num2)

showNum2()

def Uzb():
    me = "Husniddin"

    def Tashkent():
        print(me)
        global salary
        salary = 500

    def Samarkand():
        print(me)
        print(salary)

    Tashkent()
    Samarkand()

Uzb()
print(salary)
