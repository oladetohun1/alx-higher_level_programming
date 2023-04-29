#!/usr/bin/python3
"""
This module defines a script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.

Usage:
    ./my_script.py <letter>

Returns:
    If the POST request is successful and the response contains a valid JSON,
    it prints the ID and name of the first user that matches the letter search.
    If the response does not contain a valid JSON, it prints "Not a valid JSON".
    If no user matches the letter search, it prints "No result".

Example:
    ./my_script.py a
"""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) < 2:
        q = ""
    else:
        q = argv[1]

    letter_search = {"q": q}
    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, letter_search)

    try:
        value_found = response.json()
        if value_found:
            print(f"{[value_found.get('id')]} {value_found.get('name')}")
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
