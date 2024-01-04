#!/usr/bin/python3
if __name__ == "__main__":

    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) not in [4]:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a, operator, b = (int(sys.argv[1]), sys.argv[2], int(sys.argv[3]))
        if operator == "+":
            result = add(a, b)
            print("{} {} {} = {}".format(a, operator, b, result))
        elif operator == "-":
            result = sub(a, b)
            print("{} {} {} = {}".format(a, operator, b, result))
        elif operator == "*":
            result = mul(a, b)
            print("{} {} {} = {}".format(a, operator, b, result))
        elif operator == "/":
            result = div(a, b)
            print("{} {} {} = {}".format(a, operator, b, result))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
