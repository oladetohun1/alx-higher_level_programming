#!/usr/bin/bash
curl --head -s "$1" | grep "Content-Length" | cut -d ' ' -f i2
