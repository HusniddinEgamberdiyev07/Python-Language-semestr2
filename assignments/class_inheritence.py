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