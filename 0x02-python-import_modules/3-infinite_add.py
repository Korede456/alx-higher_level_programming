#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argsum = 0

    if len(sys.argv) == 1:
        print("{}".format(argsum))
    else:
        for i in range(1, len(sys.argv)):
            argsum += (int(sys.argv[i]))
        print("{}".format(argsum))
