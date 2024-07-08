#!/usr/bin/python3
""" Display the x-request-id header variable of a request to a given url """

import urllib.request
from sys import argv

if __name__ == '__main__':

    req = urllib.request.Request(argv[1])
    with urllib.request.urlopen(req) as response:
                print(dict(response.headers).get("X-Request-Id"))
