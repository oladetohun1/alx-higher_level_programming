#!/usr/bin/python3
""" a Python script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable found in the header of the
response. """

import request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = request.get(url)
    print(req.headers.get('X-Request-Id'))
