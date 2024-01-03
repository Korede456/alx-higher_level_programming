#!/usr/bin/python3
def print_last_digit(number):
    pass


def print_last_digit(number):
    if number >= 0:
        ldigit = number % 10
        print(f"{ldigit}", end="")
        return ldigit
    else:
        ldigit = (number % -10) * (-1)
        print(f"{ldigit}", end="")
        return ldigit
