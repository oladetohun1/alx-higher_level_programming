#!/bin/bash
# Displays the body of the response of a curl POST requests
curl -sX POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
