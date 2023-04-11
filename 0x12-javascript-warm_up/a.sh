#!/usr/bin/bash
read -p "write your custom message:" message
git add .
git commit -m'$message'
git push
