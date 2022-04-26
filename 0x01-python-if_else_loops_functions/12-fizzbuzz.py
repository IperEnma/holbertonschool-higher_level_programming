#!/usr/bin/python3
def fizzbuzz():
    for x in range(1, 101):
        if not(x % 15):
            print("FizzBuzz", end=" ")
        elif not(x % 5):
            print("Buzz", end=" ")
        elif not(x % 3):
            print("Fizz", end=" ")
        else:
            print("{}".format(x), end=" ")
