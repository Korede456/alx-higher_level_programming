#!/usr/bin/python3
"""
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
    return result """
def safe_print_division(a, b):
    result = None
    
    try:
        # Perform the division
        result = a / b
    
    except ZeroDivisionError:
        # Handle the case where division by zero occurs
        print("Error: Division by zero")
    
    except Exception as e:
        # Handle other exceptions
        print("Error:", e)
    
    finally:
        # Print the result or a message if there was an error
        if result is not None:
            print("Inside result: {}".format(result))
        else:
            print("Inside result: None")
    
    return result

