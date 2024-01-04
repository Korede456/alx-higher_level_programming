#!/usr/bin/python3
if __name__ = "__main__":

    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) not 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a, operator, b = (int(sys.argv[1]), sys.argv[2], int(sys.argv[3]))
        match operator:
            case "+":
                result = add(a, b)
                print("{} {} {} = {}".format(a, operator, b, result))
            case "-":
                result = sub(a, b)
                print("{} {} {} = {}".format(a, operator, b, result))
            case "*":
                result = mul(a, b)
                print("{} {} {} = {}".format(a, operator, b, result))
            case "/":
                result = div(a, b)
                print("{} {} {} = {}".format(a, operator, b, result))
            case _:
                print("Unknown operator. Available operators: +, -, * and /")
                sys.exit(1)
