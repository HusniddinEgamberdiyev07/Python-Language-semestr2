def fibannacci(limit):
    if limit <= 0:
        print("You need positive numbers")
    elif limit == 1:
        print(1)
    else:
        num1 = 0
        num2 = 1
        count = 0

        while count < limit:
            print(num1, end=" ")
            
            num3 = num1 + num2

            num1 = num2
            num2 = num3
            count+=1

fibannacci(10)
