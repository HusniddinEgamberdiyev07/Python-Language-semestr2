grades = [
    {
        "name":"technical english",
        "grade":10
    },
    {
        "name":"technical english",
        "grade":90
    },
    {
        "name":"technical english",
        "grade":70
    },
    {
        "name":"technical english",
        "grade":60
    },
    {
        "name":"technical english",
        "grade":59
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
    elif(function == "grade"):
        passed = "passed"
        mark = "F"

        for grade in grades:
            if(grade["grade"] > 90):
                mark = "A"
            elif(grade["grade"] > 80):
                mark = "B"
            elif(grade["grade"] > 70):
                mark = "C"
            elif(grade["grade"] > 60):
                mark = "D"
            else:
                mark = "F"
                passed = "failed"

            print("Subject: ", grade["name"])
            print("Mark: ", mark, passed)

calc_grades(input("Enter your function: "))