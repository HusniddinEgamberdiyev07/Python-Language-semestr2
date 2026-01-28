def factorial(num):
    factorial =1
    if(num < 0):    print("No factorial") 
    elif(num == 0): print(1)
    else:
        for i in range(num, 0, -1):
            factorial *= i
        print(factorial)
            
factorial(4)