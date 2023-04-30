#!/bin/bash
# Displays the body of the response of a curl POST requests
curl -sLX PUT -d "user_id=98" -H "Origin:" 0.0.0.0:5000/catch_me
