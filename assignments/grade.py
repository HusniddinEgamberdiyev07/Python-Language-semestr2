grades = [
    {
        "name":"technical english",
        "grade":10
    },
    {
        "name":"technical english",
        "grade":10
    },
    {
        "name":"technical english",
        "grade":10
    },
    {
        "name":"technical english",
        "grade":10
    },
    {
        "name":"technical english",
        "grade":10
    },
]

def calc_grades(function):

    if(function == "total"):
        total = 0
        for grade in grades:
            total += grade["grade"]
        print(total)
    elif(function == "average"):
        avg = 0
        for grade in grades:
            avg += grade["grade"]
        avg = avg / len(grades)
        print(avg)
    elif(function == "passed"):
        passed = True
        for grade in grades:
            if(grade["grade"] < 60):
                passed = False
        print(passed)

calc_grades(input("Enter your function"))