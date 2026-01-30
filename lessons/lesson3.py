# -- Recursion --

# Recursion is function calling itself

def factorial(num):
    if num <= 0:
        print("Pls enter positive number")
    else:
        if num == 1:
            return 1

        else:
            return num*factorial(num-1)
    
# 4*f(3)
# 3*f(2)
# 2*f(1)
# 1

# 1
# 2*1
# 3*2*1
# 4*3*2*1

print(factorial(5))