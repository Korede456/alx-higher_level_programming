#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: ", end="")
    if b != 0:
        print("{}".format(result))
    else:
        print("None")
    return result
