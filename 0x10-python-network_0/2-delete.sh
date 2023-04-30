#!/bin/bash
#Bash script that sends a DELETE request to the URL passed as the first argument and display the body
curl -s $1 -X DELETE
