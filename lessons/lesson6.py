# When we add init function it will overrides parent's init

# If child has the same method name child will override that method

class Person:
    def __init__(self, name, lname):
        self.name = name
        self.lastname = lname

    def say_hi(self):
        print("Hello "+self.name)

class Student(Person):
    def __init__(self, name, lname, age):
        Person.__init__(self, lname, name)
        self.age = age

class Child(Student):
    def __init__(self, name, lname, age, school):
        Student.__init__(self, name, lname, age)
        # super().__init__(name, lname, age)
        self.school = school

    def say_hi(self):
        print("Bye")

child1 = Child("Name", "Lname", 18, "2-school")
child1.say_hi()

# -- iter & next functions --

list1 = [1, 2, 3]
list2 = iter(list1)

print(next(list2))
print(next(list2))
print(next(list2))

name = "Husniddin"
name_iter = iter(name)
print(next(name_iter))