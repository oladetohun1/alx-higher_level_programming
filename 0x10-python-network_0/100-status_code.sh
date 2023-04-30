#!/bin/bash
# Displays the size of the status code of the response of a curl requests
curl -so /dev/null -w '%{http_code}' "$1"
