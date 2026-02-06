# modifiying properties

class Car:
    def __init__(self, brand, cost):
        self.brand = brand
        self.cost = cost

    def info(self):
        print("brand: ", self.brand)
        print("cost: ", self.cost)

car1 = Car("bmw", 1000)
# car1.info()
car1.cost = 10000

# car1.info()

# Deleting property

# car1.info()
del car1.brand
# print(car1.brand) -> error

# Deleting objects

del car1
# print(car1) -> error

# Empty class

class NothingHere:
    pass




# Inheritence

# Base is the root class (parent class) or super class
# Child class is derived class or inherited class or sub class

class GrandFather:
    def __init__(self, money, house):
        self.money = money 
        self.house = house

    def open_house(self):
        print(self.house + " opened")


class Father(GrandFather):
    def __init__(self, money, house, bisnis):
        super().__init__(money, house)
        self.bisnis = bisnis

    def make_money(self):
        self.money += 5
        print("money: ", self.money)


class Child(Father):
    def __init__(self, money, house, bisnis):
        super().__init__(money, house, bisnis)
    
    def waste_money(self):
        print("money: ", self.money)
        self.money-=10
        print("money: ", self.money)
        print("money: ", self.money)
        

son = Child(100, "building", "bisnis")
son.open_house()
son.waste_money()
son.make_money()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print(self.name + " walking")

class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school

    def study(self):
        print("I am studying at ", self.school)

student1 = Student("Bot", 17, 2)
student1.walk()
student1.study()