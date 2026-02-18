# datetime module

import datetime as d

now = d.datetime.now()
print(now) # year-month-day hour:minute-second.milisecond



print("weekday", now.strftime("%A"))   # weekday, Wednesday
print(now.strftime("%a"))   # Wed

print("month", now.strftime("%B"))   # month, February
print(now.strftime("%b"))   # Feb
print("month number", now.strftime("%m"))   # month number

# sunday - 0
# monday - 1
# ...
# saturday - 6

print("weekday in index number", now.strftime("%w"))   # weekday in index number.

print("month/day/year", now.strftime("%D"))   # month/day/year
print("day", now.strftime("%d"))   # day

print("short year", now.strftime("%y"))
print("long year", now.strftime("%Y"))

print("24 hours time", now.strftime("%H"))

print("12 hours times", now.strftime("%I"))
print("12 hours . pm/am", now.strftime("%p"))

# am from midnight to noon
# pm from noon just before midnight

print("mins", now.strftime("%M"))
print("seconds", now.strftime("%S"))

print("which day we are in a year", now.strftime("%j"))



print(now.year)
print(now.month)
print(now.day)

print(now.hour)
print(now.minute)
print(now.second)

date = d.datetime(2007, 12, 11) # year, month, day
print(date)
print("I have lived ", now-date)
print(now.year - date.year)


print(now.year)
print(now.month)
print(now.day)

print(now.hour)
print(now.minute)
print(now.second)



# Math module

# bult in function

nums = [1, 2, 3, 4, 5, 66]

print("lowest", min(nums))
print("greatest", max(nums))

print(min(1, 10))
print(max(1, 10))

print(abs(-10)) # absolute

print(pow(2, 5)) # num, power
print(pow(25, 1/2)) # sqr root

print(round(2.26, 1)) # num, decimal places

# math module methods

import math

print(math.sqrt(25)) # squere root

print(math.ceil(2.24))  # rounds up
print(math.floor(2.26)) # rounds down
print(math.pi)
