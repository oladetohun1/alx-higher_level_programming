#!/bin/bash
# Displays the body of the response of a curl POST requests
curl -s -X PUT 0.0.0.0:5000/catch_me -d "You got me!"
