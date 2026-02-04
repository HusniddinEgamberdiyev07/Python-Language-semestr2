# -- Classes & objects --

# c++ is the first oop lang

# Classes are blueprints for objects
# We will create objects using classes

# Objects has properties and methods

# to create a class use class keyword

# class ClassName:
#   properties
#   methods

class Class:
    x=5

print(Class)
print(Class.x)
print(type(Class))

obj1 = Class()
print(obj1.x)

# to create an object 
# varaiableName = ClassName()



class Human:
    legs = 2
    arms = 2
    eyes = 2
    nose = 1
    ears = 2

    def __init__(self, height, weight, name):
        self.name = name
        self.height = height
        self.weight = weight


husniddin = Human("63cm", "45kg", "Husniddin")
print(husniddin.name)

class Father:

    def __init__(self, money, house, car):
        self.money = money
        self.house = house
        self.car = car

son = Father(1000, "somewhere", "car1")
son2 =  Father(10000, "somewhere2", "car2")
print(son.money)
print(son2.house)

# __init__ is a built in function. Every class has init function.
# it will executed whenever we call the class.
# Use it to assign values to object properties
# __init__ function always has self parameter

# self can access the variables that belongs to the class
# in init it stores the value in that object
# self is always the first paarm in init

class Person():
    def __init__(self, name, age):
        self.name  = name
        self.age = age

    def talk(self):
        print("Hi " + self.name)


person1 = Person("Husniddin", 18)
person2 = Person("Sardor", 18)
print(person1.name)
print(person2.name)
person1.talk()
person2.talk()

# obj inside list
list = [Person("Someone", 0)]
list[0].talk()

class P:
    def __init__(me, name):
        me.name = name

husniddin1 = P("Husniddin")