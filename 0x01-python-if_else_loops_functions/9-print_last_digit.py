#!/usr/bin/python
def print_last_digit(number):
    pass


def print_last_digit(number):
    if number >= 0:
        ldigit = number % 10
        return ldigit
    else:
        ldigit = number % -10
        return ldigit
