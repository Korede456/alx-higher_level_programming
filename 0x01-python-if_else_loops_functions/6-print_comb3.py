#!/usr/bin/python3
for tens in range(10):
    for ones in range(tens + 1, 10):
        if ones and tens in [8, 9]:
            print("{:d}{:d}".format(tens, ones), end=("\n"))
        else:
            print("{:d}{:d}".format(tens, ones), end=", ")
