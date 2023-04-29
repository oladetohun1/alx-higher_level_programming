#!/usr/bin/python3
""" a Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter. """

import requests
import sys

if __name__ == "__main__":
    '''
    if the letter is sent, it must be sent as a letter parameter of the
    request and if the response body is properly JSON formatted and not empty,
    display the id and name like this: [<id>] <name>
    Otherwise:
        Display Not a valid JSON if the JSON is invalid
        Display No result if the JSON is empty
    '''
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    letter_search = {"q": letter}
    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, letter_search)
    print(response.content)

    try:
        json_response = response.json()
        if json_response:
            print(f"{[json_response.get('id')]} {json_response.get('name')}")
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
