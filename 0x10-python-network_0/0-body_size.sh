#!/usr/bin/bash
curl -sI $1 | grep  -i Content-Length | awk '{print $2}'
