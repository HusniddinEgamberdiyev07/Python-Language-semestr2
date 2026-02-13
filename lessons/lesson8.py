# -- modules --

# libraries are modules.

# We don't need to wright whole application in one file.
# We can import code from another file using import keyword

import lesson8_import as m

m.helloWorld()
m.sayHi(m.name)
print(m.add(1, 2))

# from lesson8_import import helloWorld, sayHi, add

# helloWorld()
# sayHi("Husniddin")
# print(add(1, 2))

for key in m.people.keys():
    print(key, m.people[key])