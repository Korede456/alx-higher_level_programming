#!/usr/bin/python3
def fizzbuzz():
    pass


def fizzbuzz():
    for i in range(1, 101):
        if (i % 3) == 0 and (i % 5) == 0:
            print("FizzBuzz")
        if (i % 3) == 0:
            print("Fizz")
        if (i % 5) == 0:
            print("Buzz")
        if i != 100:
            print(" ")
