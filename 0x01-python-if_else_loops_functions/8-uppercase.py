#!/usr/bin/python3
def uppercase(str):
    for strs in str:
        if ord(strs) >= ord('a') and ord(strs) <= ord('z'):
            strs = chr(ord(strs) - 32)
        print("{}".format(strs), end='')
    print()
