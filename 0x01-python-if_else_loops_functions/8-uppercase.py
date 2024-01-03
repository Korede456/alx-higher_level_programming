#!/usr/bin/python3
def uppercase(str):
    pass


def uppercase(str):
    newstr = ""
    for i in range(0, len(str) - 1):
        if 97 <= ord(str[i]) <= 122:
            newstr = newstr + (chr(i - 32))
        else:
            newstr = newstr + (chr(i))
    print("{:s}".format(newstr))
