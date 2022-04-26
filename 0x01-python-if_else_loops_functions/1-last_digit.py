#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number == 0:
    print("Last digit of 0 is 0 and is 0")
    return
if (number/abs(number))*(abs(number) % 10) > 5:
    print(f"Last digit of {number}\
 is {int(number/abs(number))*(abs(number) % 10)}\
 and is greater than 5")
elif (number/abs(number))*(abs(number) % 10) == 0:
    print(f"Last digit of {number}\
 is {int(number/abs(number))*(abs(number) % 10)} and is 0")
else:
    print(f"Last digit of {number}\
 is {int(number/abs(number))*(abs(number) % 10)}\
 and is less than 6 and not 0")
